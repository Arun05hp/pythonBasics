class TagCloud:
    def __init__(self):
        self.__tags = {}

    def add(self,tag):
        self.__tags[tag] = self.__tags.get(tag, 0 ) + 1     # get(tag,0) if tag present it return tag else 0

    def __getitem__(self,tag):
        return self.__tags.get(tag,0)

    def __setitem__(self,tag,count):
        self.__tags[tag] = count

    def __len__(self):
        return len(self.__tags)

    def __iter__(self):
        return iter(self.__tags)

cloud = TagCloud()
cloud.add("Ak")
cloud.add("Ak")
cloud.add("Ak")
cloud.add("ak")

cloud["ak"]

cloud["ak"] = 10
len(cloud)
# print(cloud.__tags)
# print(cloud.__tags["ak"])
print("len: ",len(cloud))

for tag in cloud:
    print(tag)

print(cloud.__dict__)
