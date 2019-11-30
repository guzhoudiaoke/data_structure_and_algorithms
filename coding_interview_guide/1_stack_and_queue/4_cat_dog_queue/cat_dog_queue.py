import random


class Pet:
    def __init__(self, no):
        self.no = no

    
    def get_type(self):
        return self.type

    
    def get_no(self):
        return self.no


class Cat(Pet):
    def __init__(self, no):
        self.type = 'cat'
        Pet.__init__(self, no)


class Dog(Pet):
    def __init__(self, no):
        self.type = 'dog'
        Pet.__init__(self, no)


class PetQueueItem:
    def __init__(self, pet, timestamp):
        self.pet = pet
        self.timestamp = timestamp


    def get_pet(self):
        return self.pet


    def get_timestamp(self):
        return self.timestamp


    def get_type(self):
        return self.pet.get_type()


class DogCatQueue:
    def __init__(self):
        self.dog_queue = []
        self.cat_queue = []
        self.timestamp = 0


    def add(self, pet):
        if pet.get_type() == 'dog':
            self.dog_queue.append(PetQueueItem(pet, self.timestamp))
        elif pet.get_type() == 'cat':
            self.cat_queue.append(PetQueueItem(pet, self.timestamp))
        else:
            raise Exception('Error pet type')

        self.timestamp += 1


    def poll(self):
        if self.empty():
            raise Exception('Queue is empty')

        if self.dog_empty():
            return self.cat_queue.pop(0)

        if self.cat_empty():
            return self.dog_queue.pop(0)

        if self.dog_queue[0].get_timestamp() < self.cat_queue[0].get_timestamp():
            return self.dog_queue.pop(0)
        else:
            return self.cat_queue.pop(0)


    def poll_dog(self):
        if self.dog_empty():
            raise Exception('Dog Queue is empty')

        return self.dog_queue.pop(0)


    def poll_cat(self):
        if self.cat_empty():
            raise Exception('Cat Queue is empty')

        return self.cat_queue.pop(0)


    def empty(self):
        return self.dog_empty() and self.cat_empty()


    def dog_empty(self):
        return len(self.dog_queue) == 0


    def cat_empty(self):
        return len(self.cat_queue) == 0


def test_pet():
    c = Cat()
    print(c.get_type())
    d = Dog()
    print(d.get_type())


def get_rand_no(d, maxno):
    while True:
        no = random.randint(0, maxno)
        if no not in d:
            d[no] = True
            return no


def test_queue(times, maxno):
    cat_queue = []
    dog_queue = []
    queue = []
    cat_dog_queue = DogCatQueue()
    no_dir = {}

    for _ in range(times):
        op = random.randint(0, 8)
        if op == 0:
            # add dog
            no = get_rand_no(no_dir, maxno)
            dog_queue.append(Dog(no))
            queue.append(Dog(no))
            cat_dog_queue.add(Dog(no))
        elif op == 1:
            # add cat
            no = get_rand_no(no_dir, maxno)
            cat_queue.append(Cat(no))
            queue.append(Cat(no))
            cat_dog_queue.add(Cat(no))
        elif op == 2:
            # poll dog
            if len(dog_queue) == 0:
                if not cat_dog_queue.dog_empty():
                    raise Exception('Error dog queue')
            else:
                d1 = dog_queue.pop(0)
                d2 = cat_dog_queue.poll_dog()
                for i in range(len(queue)):
                    if queue[i].get_no() == d1.get_no():
                        queue.pop(i)
                        break

                if d1.get_no() != d2.get_pet().get_no():
                    raise Exception('Error poll dog')
                print('poll dog', d1.get_no())
                no_dir.pop(d1.get_no())
        elif op == 3:
            # poll cat
            if len(cat_queue) == 0:
                if not cat_dog_queue.cat_empty():
                    raise Exception('Error cat queue')
            else:
                c1 = cat_queue.pop(0)
                c2 = cat_dog_queue.poll_cat()
                for i in range(len(queue)):
                    if queue[i].get_no() == c1.get_no():
                        queue.pop(i)
                        break

                if c1.get_no() != c2.get_pet().get_no():
                    raise Exception('Error poll cat')
                print('poll cat', c1.get_no())
                no_dir.pop(c1.get_no())
        elif op == 4:
            # poll
            if len(queue) == 0:
                if not cat_dog_queue.empty():
                    raise Exception('Error queue')
            else:
                p = queue.pop(0)
                if len(cat_queue) != 0 and p.get_no() == cat_queue[0].get_no():
                    cat_queue.pop(0)
                else:
                    dog_queue.pop(0)
                p2 = cat_dog_queue.poll()
                if p.get_no() != p2.get_pet().get_no():
                    raise Exception('Error poll')
                print('poll pet', p.get_no())
                no_dir.pop(p.get_no())

        elif op == 5:
            # empty
            b1 = len(dog_queue) == 0 and len(cat_queue) == 0
            b2 = len(queue) == 0
            b3 = cat_dog_queue.empty()
            if b1 != b2 or b2 != b3:
                raise Exception('Error empty')
        elif op == 6:
            # dog empty
            b1 = len(dog_queue) == 0
            b2 = cat_dog_queue.dog_empty()
            if b1 != b2:
                raise Exception('Error dog empty')
        elif op == 7:
            # cat empty
            b1 = len(cat_queue) == 0
            b2 = cat_dog_queue.cat_empty()
            if b1 != b2:
                raise Exception('Error cat empty')


if __name__ == '__main__':
    test_queue(500, 10000)

