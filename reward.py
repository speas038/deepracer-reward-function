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
    progress = params['progress'] #Add an incentive eventually.  Higher rewards the closer you are to finishing
    
    
    #incentivise being closer to the border when turning
    if all_wheels_on_track == False:
        print ("All wheels off track_width")
        return 1e-3
    
    
    #for higher steering angle give higher reward
    
    
    # Steering penality threshold, change the number based on your action space setting
    ABS_STEERING_THRESHOLD = 20 

    # Penalize reward if the car is steering too much
    if abs_steering > ABS_STEERING_THRESHOLD:
        reward *= 0.8

    print (params)
    print("reward: {}".format(reward))
    
    return float(reward)
