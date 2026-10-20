# Life-cycle of Thread

# difference b/w - 
    # 1. creating & starting
    # 2. run & start
    # 3. blocked & terminated

# New Thread -> (running thread -> <- Blocked thread)
# then from running thread -> terminated thread

# New Thread(Thread.new) -> Runnable, when Thread.run <- Sleeping(when runnable waiting for I/O)
# Runnable has two reason to terminate  - (1) Terminate with exception when exception raise (2) Terminate normally when Thread.exit

