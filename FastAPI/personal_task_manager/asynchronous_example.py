# import time

# def brewCoffee():
#     print("Start brewCoffee...")
#     time.sleep(3)
#     print("End brewCoffee...")
#     return "Coffee ready"

# def toastBagel():
#     print("Start toastBagel...")
#     time.sleep(3)
#     print("End toastBagel...")
#     return "Bagel toasted"

# def main():
#     start_time = time.time()

#     result_coffee = brewCoffee()
#     result_bagel = toastBagel()

#     end_time = time.time()
#     elapsed_time = end_time - start_time

#     print(f"Result of brewCoffee: {result_coffee}")
#     print(f"Result of toastBagel: {result_bagel}")
#     print(f"Total execution time: {elapsed_time:.2f} seconds")

# if __name__ == "__main__":
#     main()

#################################################################

import asyncio
import time

# coroutine function
async def brewCoffee():
    print("Start brewCoffee...")
    await asyncio.sleep(3)
    print("End brewCoffee...")
    return "Coffee ready"

# coroutine function
async def toastBagel():
    print("Start toastBagel...")
    await asyncio.sleep(3)
    print("End toastBagel...")
    return "Bagel toasted"

async def main():
    start_time = time.time()

    batch = asyncio.gather(brewCoffee(), toastBagel())
    result_coffee, result_bagel = await batch

    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"Result of brewCoffee: {result_coffee}")
    print(f"Result of toastBagel: {result_bagel}")
    print(f"Total execution time: {elapsed_time:.2f} seconds")

# Run the main coroutine
if __name__ == "__main__":
    asyncio.run(main())

#################################################################

# import asyncio
# import time

# async def brewCoffee():
#     print("Start brewCoffee...")
#     await asyncio.sleep(3)
#     print("End brewCoffee...")
#     return "Coffee ready"

# async def toastBagel():
#     print("Start toastBagel...")
#     await asyncio.sleep(3)
#     print("End toastBagel...")
#     return "Bagel toasted"

# async def main():
#     start_time = time.time()

#     coffee_task = asyncio.create_task(brewCoffee())
#     toast_task = asyncio.create_task(toastBagel())

#     result_coffee = await coffee_task
#     result_bagel = await toast_task

#     end_time = time.time()
#     elapsed_time = end_time - start_time

#     print(f"Result of brewCoffee: {result_coffee}")
#     print(f"Result of toastBagel: {result_bagel}")
#     print(f"Total execution time: {elapsed_time:.2f} seconds")

# if __name__ == "__main__":
#     asyncio.run(main())

# python asynchronous_example.py