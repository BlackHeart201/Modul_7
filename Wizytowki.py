class People:
    def __init__(self, name, surname, company, position, mail):
        self.name = name
        self.surname = surname
        self.company = company
        self.position = position
        self.mail = mail

    def __repr__(self):
        return f'{self.name} {self.surname} {self.company} {self.position} {self.mail}'

    def __eq__(self, other):
        return all(
            (
                self.name == other.name,
                self.surname == other.surname,
                self.company == other.company,
                self.position == other.position,
                self.mail == other.mail
            )
        )


person_one = People(name="Beatrycze", surname="Majewska", company="Hughes & Hatcher",
                    position="Press secretary", mail="BeatryczeMajewska@teleworm.us")
person_two = People(name="Krystyna", surname="Nowakowska", company="Great American Music",
                    position="Television camera operator", mail="KrystynaNowakowska@teleworm.us")
person_three = People(name="Joasia", surname="Wieczorek", company="Rickel",
                      position="Motor coach driver", mail="JoasiaWieczorek@teleworm.us")
person_four = People(name="Maryla", surname="Tomaszewska", company="Total Serve",
                     position="Wildlife biologist", mail="MarylaTomaszewska@teleworm.us")
person_five = People(name="Stanisław", surname="Michalski", company="Bold Ideas",
                     position="Park naturalist", mail="StanislawMichalski@teleworm.us")

people_base = [person_one, person_two, person_three, person_four, person_five]
by_name = sorted(people_base, key=lambda people: people.name)
by_surname = sorted(people_base, key=lambda people: people.surname)
by_mail = sorted(people_base, key=lambda people: people.mail)
