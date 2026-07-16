# Iterators in Python

# Custom Iterator Class that behaves like a range() function
class RemoteControl:
    def __init__(self):
        self.channels = ["HBO", "CNN", "ESPN", "Discovery"]
        self.index = -1

    # An Iterable must return an Iterator object via __iter__
    def __iter__(self):
        return self

    # An Iterator must define __next__ to return items one by one
    def __next__(self):
        self.index += 1
        if self.index >= len(self.channels):
            # Must raise StopIteration when done
            raise StopIteration
        return self.channels[self.index]

# Create our custom iterator
remote = RemoteControl()
itr = iter(remote) # calls __iter__

# Manual iteration using next()
print(next(itr))  # HBO
print(next(itr))  # CNN

print("-" * 20)

# Automatic iteration using a for loop
# (A new remote object is needed as the previous one is exhausted)
new_remote = RemoteControl()
for channel in new_remote:
    print(channel)
