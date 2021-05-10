# According to the task I suppose that different types of predators can't live in one corral.
# Different types of habivores has to strategies or live separately or live together.
# To implement second idea you have to uncoment the commented code and comment the parallel logic for the first idea
AREA = 3400000
TASK_STRATEGY = 1

predators = {
    'lion': 12,
    'panther': 12,
    'lynx': 10,
    'bear': 7,
    'crocodile': 8,
    'cheetah': 10,
}
herbivorous = {
    'monkey': 2,
    'deer': 9,
    'roe': 5,
    'hare': 1,
    'raccon': 1,
    'horse': 12,
}

corrals = {}
area = 0

with open('input.txt', 'r') as input:
    n = int(input.readline().strip())
    animals = input.readline().split()


def locate_animals_separately():
    """
        Locating animals, when every animal type has separate corral
    """
    global area
    for animal in animals:
        if animal in [*predators.keys(), *herbivorous.keys()]:
            if animal in corrals.keys():
                corrals[animal] += 1
            else:
                corrals[animal] = 1 # every animal type has separate corral
            area += predators.get(animal, herbivorous.get(animal))
        else:
            print(f'Unrecognized animal: {animal}')


def locate_animals_by_type():
    """
        Locating animals, when every predator type has separate corral
        and all harbivorous are placed in one corral
    """
    global area
    for animal in animals:
        if animal in [*predators.keys(), *herbivorous.keys()]:
            if animal in corrals.keys():
                corrals[animal] += 1
            elif animal in herbivorous.keys():
                corrals['herbivorous'] = corrals.get('herbivorous', 0) + 1
            else:
                corrals[animal] = 1
            area += predators.get(animal, herbivorous.get(animal))
        else:
            print(f'Unrecognized animal: {animal}')


def locate_in_corrals(animal, corrals):
    """
        Check corrals one by one for avalability to locate new animal.
        Herbivorous can't live with predator in one corral
    """
    for corral in corrals:
        if animal == corral:
            corrals[corral] += 1
        elif animal in predators == corral in predators:
            continue
            # if animal in herbivorous and corral == 'herbivorous':
            #     corrals[corral] += 1
        else:
            print(f'{animal} and {corral} can\'t live in one corral')


if TASK_STRATEGY == 1:
    locate_animals_separately()

    if area > AREA:
        print('Not enough area for new animals!')
    else:
        print(f'Area needed: {area} m^2')
        print(f'Number of corrals: {len(corrals)}')
        print(f'Animal type    | Number of animals')
        print('----------------------------------')
        with open('corrals.txt','r+') as output:
            output.truncate(0)
        with open('corrals.txt', 'a+') as output:
            output.write(str(len(corrals)) + '\n')
            for animal_type in corrals:
                space = (15 - len(animal_type)) * ' '
                print(f'{animal_type}{space}| {corrals[animal_type]}')
                output.write(f'{animal_type} {corrals[animal_type]}\n')
elif TASK_STRATEGY == 2:
    error = False
    with open('corrals.txt', 'r') as input:
        n = int(input.readline())
        for _ in range(n):
            key, value = input.readline().split()
            corrals[key] = int(value)
    for animal in animals:
        if animal in [*predators.keys(), *herbivorous.keys()]:
            # locate_in_corrals(animal, corrals)
            if animal in corrals.keys():
                corrals[animal] += 1
            else:
                corrals[animal] = 1 # if it's possible to build new corrals for new animal types
                # print(f"Can't locate {animal} in our zoo!")
                # error = True
                # break
            area += predators.get(animal, herbivorous.get(animal))
        else:
            print(f'Unrecognized animal: {animal}')
    
    if area > AREA:
        print('Not enough area for new animals!')
    elif not error:
        print(f'Area needed: {area}')
        print(f'Number of corrals: {len(corrals)}')
        print(f'Animal type    | Number of animals')
        print('----------------------------------')
        with open('corrals.txt','r+') as output:
            output.truncate(0)
        with open('corrals.txt', 'a+') as output:
            output.write(str(len(corrals)) + '\n')
            for animal_type in corrals:
                space = (15 - len(animal_type)) * ' '
                print(f'{animal_type}{space}| {corrals[animal_type]}')
                output.write(f'{animal_type} {corrals[animal_type]}\n')
    else:
        print("Type mismatch. Can't locate new animals in our zoo!")