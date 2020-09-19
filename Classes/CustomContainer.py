class TagCloud:
    def __init__(self):
        self.tags = {}

    def add(self,tag):
        self.tags[tag] = self.tags.get(tag, 0 ) + 1     # get(tag,0) if tag present it return tag else 0

    def __getitem__(self,tag):
        return self.tags.get(tag,0)

    def __setitem__(self,tag,count):
        self.tags[tag] = count

    def __len__(self):
        return len(self.tags)

    def __iter__(self):
        return iter(self.tags)

cloud = TagCloud()
cloud.add("Ak")
cloud.add("Ak")
cloud.add("Ak")
cloud.add("ak")

cloud["ak"]

cloud["ak"] = 10
len(cloud)
print(cloud.tags)
print("len: ",len(cloud))

for tag in cloud:
    print(tag)
