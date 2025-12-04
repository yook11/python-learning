def findMergeNode(headA, headB):
    # --- 1. 長さを計算する（ここは同じ） ---
    current_a = headA
    current_b = headB
    length_a = 0
    length_b = 0

    while current_a is not None:
        current_a = current_a.next
        length_a += 1
    
    while current_b is not None:
        current_b = current_b.next
        length_b += 1
    
    # --- 2. スタート位置を合わせる（ここも同じ） ---
    if length_a > length_b:
        long = headA
        short = headB
        len_diff = length_a - length_b
    else:
        long = headB
        short = headA
        len_diff = length_b - length_a
    
    for _ in range(len_diff):
        long = long.next
    
    # --- 3. 同時に進みながらチェックする ---
    while long is not None and short is not None:

        if long.data == short.data:
            temp_long = long
            temp_short = short
            is_match = True

            while temp_long is not None and temp_short is not None:
                if temp_long.data != temp_short.data:
                    is_match = False
                    break
                temp_long = temp_long.next
                temp_short = temp_short.next
            if is_match:
                return long.data
        
        long = long.next
        short = short.next
    return -1
        
        
            
