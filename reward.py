def reward_function(params):
    '''
    Example of rewarding the agent to follow center line
    '''
    
    # Read input parameters
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    abs_steering = abs(params['steering_angle']) # Only need the absolute steering angle
    steering_angle = params['steering_angle']
    all_wheels_on_track = params['all_wheels_on_track']
    progress = params['progress'] #Add an incentive eventually.  Higher rewards the close
    is_left_of_center = params['is_left_of_center']
    
    
    #incentivise being closer to the border when turning
    if all_wheels_on_track == False:
        print ("All wheels off track_width")
        return 1e-3
    
    
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
    
    if 5 <= steering_angle <= 30 and not is_left_of_center:
        reward *= .8
        
    if -5 <= steering_angle <= -30 and is_left_of_center:
        reward *= .8
        
    
    # Steering penality threshold, change the number based on your action space setting
    ABS_STEERING_THRESHOLD = 20 

    # Penalize reward if the car is steering too much
    if abs_steering > ABS_STEERING_THRESHOLD:
        reward *= 0.8

    print (params)
    print("reward: {}".format(reward))
    
    return float(reward)
