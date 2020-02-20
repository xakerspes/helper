start,end = 0,1000
capacity = 5
shag_multiply = 100
ring_buffer = RingBuffer(capacity=capacity, dtype=np.int)
while start<end:
    if start>shag_multiply:
        ring_buffer.append(start)
        if (len(ring_buffer)==capacity and 
            (ring_buffer[-1]-ring_buffer[0]==capacity-1)):
            ring_buffer = RingBuffer(capacity=capacity, dtype=np.int)
            if (start//shag_multiply + 1<end):
                print((start //shag_multiply + 1)*shag_multiply,'----')
                start = (start //shag_multiply + 1)*shag_multiply
    
    start+=1
    print(start)
