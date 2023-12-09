
# constraint is given that 
#BLOCK SIZE MUST BE LESS THAN CONTAINER COUNT 

#K is the required block number 
#B no of blocks present per container
#input we need no of blocks(B);

def get_position(K, B, container_num): 
        if container_num % 2 == 0:
            position_reverse_order = B - K % B + 1
            return position_reverse_order # for reverse order of blocks...
        else:
            posi_forward_order = K % B
            return posi_forward_order # for forward order of blocks... 
   
def find(K, B):
    container_count = 0
    for i in range(K):
        if i % B == 0:
            container_count += 1
        position = get_position(K, B, container_count)
    return container_count, position


