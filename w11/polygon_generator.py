def counter(start,end):
    start-=1 ## To start with same given value.
    end-=1
    def inner():
        nonlocal start
        nonlocal end
        if start < end:
            start+=1
            return start
        else:
             raise StopIteration()
    return inner




# cnt = counter(0,5)

# for i in range(0,5):
#     try:
#         print(cnt())
#     except Exception as e:
#         print(e)
