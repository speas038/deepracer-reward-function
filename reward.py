def reward_function(params):
    
    print("WELCOME")
    print(params)

    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    abs_steering = abs(params['steering_angle']) # Only need the absolute steering angle
    steering_angle = params['steering_angle']
    all_wheels_on_track = params['all_wheels_on_track']
    progress = params['progress'] #Add an incentive eventually.  Higher rewards the close
    is_left_of_center = params['is_left_of_center']
    speed = params['speed']
    
    reward = normalize_speed(speed, abs_steering)
    
    #incentivise being closer to the border when turning
    if all_wheels_on_track == False:
        print ("All wheels off track_width")
        return 1e-3
    
    '''   
    # Calculate 3 markers that are at varying distances away from the center line
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width
    
    
    # Give higher reward if the car is closer to center line and vice versa if straight or higher turning angles means you should be closer to the track border[p-/.]
    if distance_from_center <= marker_1 and 0 <= abs_steering <= 10:
        reward = 1.0
    elif distance_from_center <= marker_2 and 10 <= abs_steering <= 20:
        reward = 1.0
    elif distance_from_center <= marker_3 and 20 < abs_steering:
        reward = 1.0
    else:
        reward = 1e-3  # likely crashed/ close to off track
    '''
    
    if 10 <= steering_angle <= 30 and not is_left_of_center:
        reward *= .8
        
    if -10 <= steering_angle <= -30 and is_left_of_center:
        reward *= .8


    
    # Steering penality threshold, change the number based on your action space setting
    ABS_STEERING_THRESHOLD = 25

    # Penalize reward if the car is steering too much
    if abs_steering > ABS_STEERING_THRESHOLD:
        reward *= 0.8

#    print (params)
    print("calculated unweighted reward: {}".format(reward))

    #Everything else accounts for .80% of reward, and progress the remaining 20%

    weighted_progress_component = progress/100 * .20
    weighted_calculated_reward = reward * .80
    final_reward = weighted_calculated_reward + weighted_progress_component

    print("Weighted progress {} weighted reward {}".format(weighted_progress_component, weighted_calculated_reward))

    print("Final reward: {}".format(final_reward))

    return float(weighted_progress_component + weighted_calculated_reward)

def normalize_speed(speed, abs_steering):
    #Lets say we are happy with a 1m/s slowdown per 10Degrees
    ANGLE_ADJUST = .012 * abs_steering
    normalized_speed = speed/5 + ANGLE_ADJUST
    print("Normalize speed returning {}".format(normalized_speed) )
    return float(normalized_speed)
    


##TESTS##



params = {'speed':5,
          'track_width': 6,
          'distance_from_center': 4,
          'steering_angle':-25,
          'all_wheels_on_track':True,
          'progress': 100,
          'is_left_of_center': True}


reward_function(params)
