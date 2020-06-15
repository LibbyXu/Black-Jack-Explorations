def blackjack_hand_greater_than(hand_1,hand_2):
    HAND_1_new = hand_1
    HAND_2_new = hand_2
    len_1=int(len(hand_1))
    len_2=int(len(hand_2))
    for i in range(0,len_1):
        if hand_1[i] == 'J' or hand_1[i] == 'Q' or hand_1[i] == 'K':
            HAND_1_new[i] = '10'
    for i in range(0,len_2):
        if hand_2[i] == 'J' or hand_2[i] == 'Q' or hand_2[i] == 'K':
            HAND_2_new[i] = '10'
    num_hand_1 = 0
    num_hand_2 = 0
    NUM_ORDER_1 = []
    NUM_ORDER_2 = []
    for i in range(0,len_1):
        if hand_1[i] == 'A':
            num_hand_1 = num_hand_1 + 1
            NUM_ORDER_1.append(i)
    #print num_hand_1
    for i in range(0,len_2):           
        if hand_2[i] == 'A':
            num_hand_2 = num_hand_2 + 1
            NUM_ORDER_2.append(i)  
    #print num_hand_2
    
    HAND_1_order = HAND_1_new
    HAND_2_order = HAND_2_new
    
    if num_hand_1 != 0:
        for i in range(0,num_hand_1):
            HAND_1_order.remove('A') 
    if num_hand_2 != 0:
        for i in range(0,num_hand_2):
            HAND_2_order.remove('A')
     
    result_temp_1 = [int(ii) for ii in HAND_1_order]
    result_temp_2 = [int(ii) for ii in HAND_2_order]
    total_temp_1 = sum(result_temp_1)
    total_temp_2 = sum(result_temp_2)
    #print total_temp_1
    #print total_temp_2    
    if num_hand_1 == 0:
        total_final_1 = total_temp_1
    elif num_hand_1 == 1:
        if total_temp_1 <= 10:
            total_final_1 = total_temp_1 + 11
        elif total_temp_1 > 10:
            total_final_1 = total_temp_1 + 1
    elif num_hand_1 >=2:
        if total_temp_1 <= 10-num_hand_1 + 1:
            total_final_1 = total_temp_1 + 11 + num_hand_1 - 1
        elif total_temp_1 > 10-num_hand_1+1:
            total_final_1 = total_temp_1 + num_hand_1
    
    if num_hand_2 == 0:
        total_final_2 = total_temp_2
    elif num_hand_2 == 1:
        if total_temp_2 <= 10:
            total_final_2 = total_temp_2 + 11
        elif total_temp_2 > 10:
            total_final_2 = total_temp_2 + 1
    elif num_hand_2 >=2:
        if total_temp_2 <= 10-num_hand_2+1:
            total_final_2 = total_temp_2+11+num_hand_2-1
        elif total_temp_2 > 10-num_hand_2+1:
            total_final_2 = total_temp_2 + num_hand_2
            
    if total_final_2 > 21 and total_final_1 <= 21:
        print True
    elif total_final_2 <= 21 and total_final_1 <= 21:
        print total_final_1 > total_final_2
    elif total_final_1 > 21 and total_final_2 <= 21:
        print False
    elif total_final_1 > 21 and total_final_2 > 21:
        print False
    print(total_final_1)
    print(total_final_2)
            
#   return total_final_1 > total_final_2    

blackjack_hand_greater_than(['K'],['3','4'])
blackjack_hand_greater_than(['K'],['10'])
blackjack_hand_greater_than(['K','K','2'],['3'])
blackjack_hand_greater_than(['J','A','A','2'],['9','6','K','A','5','J'])
blackjack_hand_greater_than(['2','A','5','Q','4'],['J','4','3','A','10'])