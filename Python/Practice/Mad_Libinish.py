__author__ = 'Billy'

animal = raw_input("What's your favorite animal? ")
food = raw_input("What's your least favorite food? ")
rapper = raw_input("Who's your favorite rapper? ")
rhyme = raw_input("Type something that rhymes \
                    with your favorite rapper. ")
cheer = raw_input("What word do you use to cheer?! ")

print '                                        '\
      '                                        '

print '''There once was a %s from Nantucket
Who kept all of it's %s in a bucket.
But %s's friend, named %s.
Ran away with a %s
And as for the bucket, Nan took it.
%s! Funny ending, eh?''' % (
    animal, food, animal, rapper, rhyme, cheer)

