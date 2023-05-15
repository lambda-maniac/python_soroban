Section = tuple[bool, tuple[bool, ...]]
Soroban = list[Section]
Sky   = 0
Earth = 1

def structure(value: int, base: int = 10) -> Section:
    maxim = base - 1
    upper = base // 2
    lower = upper - 1

    tower = False

    if value >  maxim:
        raise ValueError(f"Cannot construct values over {maxim} @ base {base}, tried: {value}.")

    if value >= upper:
        value -= upper; tower = True

    delta = lower - value

    return ( tower
           , ( * ( True  , ) * value
             ,     False
             , * ( True  , ) * delta
             )
           )

def count(section: Section):
    value = len(section[Earth]) * section[Sky]

    for element in section[Earth]:
        if not element:
            break

        value += 1

    return value

def show(soroban: Soroban):

    length   : int = len( soroban            )
    altitude : int = len( soroban [0][Earth] )

    boundary : str = '-'.join(["#", * ["==="] * length, "#"])

    # === Sky ===
    print(boundary)

    skies = list(map(lambda section: section[Sky], soroban))
    upper = list(map(lambda value  : "<@>" if not value else " | ", skies))
    lower = list(map(lambda value  : "<@>" if     value else " | ", skies))

    print(
        ' '.join(["|", *upper, "|"])
    )
    print(
        ' '.join(["|", *lower, "|"])
    )

    # === Earth ===
    print(boundary)

    for y in range(0, altitude):

        line = []

        for x in range(0, length):
            line.append(soroban[x][Earth][y])

        print(
            ' '.join(["|", *list(map(lambda value: "<@>" if value else " | ", line)), "|"])
        )

    # === Footer ===
    print(boundary)

    print(
        "---" + '---'.join(list(map(lambda section: str(count(section)), soroban))) + "---"
    )

def generate(number: str, base: int = 10):
    return [ structure(int(digit, base = base), base) for digit in number ]
