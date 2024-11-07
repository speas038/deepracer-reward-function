def reward_function(params):
    
    # print("WELCOME")
    # print(params)

    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    abs_steering = abs(params['steering_angle']) # Only need the absolute steering angle
    steering_angle = params['steering_angle']
    all_wheels_on_track = params['all_wheels_on_track']
    progress = params['progress'] #Add an incentive eventually.  Higher rewards the close
    is_left_of_center = params['is_left_of_center']
    speed = params['speed']

    
    speed_reward = normalize_speed(speed, abs_steering)


    
    #incentivise being closer to the border when turning
    if all_wheels_on_track == False:
        # print ("All wheels off track_width")
        return 1e-3
    

    # Calculate 3 markers that are increasingly further away from the center line
    marker_1 = 0.1 * track_width
    marker_2 = 0.4 * track_width
    marker_3 = 0.7 * track_width

    # Give higher reward if the car is closer to center line and vice versa
    if distance_from_center <= marker_1:
        location_reward = 1
    elif distance_from_center <= marker_2:
        location_reward = 0.7
    elif distance_from_center <= marker_3:
        location_reward = 0.5
    else:
        location_reward = 1e-3  # likely crashed/ close to off track


    if 10 <= steering_angle <= 30 and not is_left_of_center:
        location_reward += .5
        
    if -10 <= steering_angle <= -30 and is_left_of_center:
        location_reward += .5


    
    # Steering penality threshold, change the number based on your action space setting
    ABS_STEERING_THRESHOLD = 20

    # Penalize reward if the car is steering too much
    if abs_steering > ABS_STEERING_THRESHOLD:
        speed_reward *= 0.5

#    print (params)

    #Everything else accounts for .80% of reward, and progress the remaining 20%

    weighted_progress_reward = progress/100 * .20
    weighted_speed_reward = speed_reward * .30
    weighted_location_reward = location_reward * .50

        
    final_reward = weighted_speed_reward + weighted_progress_reward + weighted_location_reward

    print("Weighted progress reward: {}".format(weighted_progress_reward))
    print("Weighted speed_reward {}".format(weighted_speed_reward))
    print("Weighted location reward: {}".format(weighted_location_reward))
    print("Location reward: {}".format(location_reward))
    print("Final reward: {}".format(final_reward))

    return float(final_reward)



#Return a value between 0 and 1 for speed ( we will weight it later)    
def normalize_speed(speed, abs_steering):
    #Lets say we are happy with a 1m/s slowdown per 10Degrees
    normalized_speed = speed/4
    return float(normalized_speed)


##TESTS##



params = {'speed':4,
          'track_width': 4,
          'distance_from_center': 2,
          'steering_angle':-2,
          'all_wheels_on_track':True,
          'progress': 100,
          'is_left_of_center': False}


reward_function(params)
