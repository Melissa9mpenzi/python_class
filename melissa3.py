#ASSIGNMENT 3
#In a python script create atleast 7 classes with a constructor with atleast 7 properties and instantiate atleast 4 classes.
#each class should have 4 objects.



class Song:
    def __init__(self,title,artiste,album,release_year,genre,duration,composer):
        self.title = title
        self.artiste = artiste
        self.album = album
        self.release_year = release_year
        self.genre = genre
        self.duration = duration
        self.composer = composer

Song1 = Song("Delusional", "Chris Brown", "Deluxe(11:11)", 2023, "R&B", "3:39", "Chris Brown")
Song2 = Song("Silence", "Khalid & Marshmello", "Single", 2017, "Dance/Electronic", "3:7", "Marshmello & Khalid")
Song3 = Song("Seasons", "Hillsong worship $ Benjamin William Hastings","The Peace Project",2017, "Gospel","4:50", "Benjamin William Hastings $ Hillsong worship")
Song4 = Song("Love Potion", "Mafikizolo", "Love Potion", 2017, "Champeta", "4:2", "Mafikizolo & Theo Kgosinkwe")

print(Song1.title)
print(Song1.artiste)
print(Song1.album)
print(Song1.release_year)
print(Song1.genre)
print(Song1.duration)
print(Song1.composer)

print(Song2.title)
print(Song2.artiste)
print(Song2.album)
print(Song2.release_year)
print(Song2.genre)
print(Song2.duration)
print(Song2.composer)

print(Song3.title)
print(Song3.artiste)
print(Song3.album)
print(Song3.release_year)
print(Song3.genre)
print(Song3.duration)
print(Song3.composer)

print(Song4.title)
print(Song4.artiste)
print(Song4.album)
print(Song4.release_year)
print(Song4.genre)
print(Song4.duration)
print(Song4.composer)


class Book:
    def __init__(self,title,author,publisher,year,genre,pages,isbn):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.year = year
        self.genre = genre
        self.pages = pages
        self.isbn = isbn

Book1 = Book("Gifted Hands", "Ben Carson", "Zondervan", 1990, "Autobiography", 224, "0310214696- ISBN 10")
Book2 = Book("The fault in our stars", "John Greene", "Dutton books", 2012, "Young Adult", 318, 9780142424179)
Book3 = Book("Me Before You", "Jojo Moyes", "Penguin", 2012, "Romance & Fiction",369, 97828811210014 )
Book4 = Book("After You","Jojo Moyes", "Penguin", 2015, "Romance novel" , 480, "0718157834-ISBN")

print(Book1.title)
print(Book1.author)
print(Book1.publisher)
print(Book1.year)
print(Book1.genre)
print(Book1.pages)
print(Book1.isbn)

print(Book2.title)
print(Book2.author)
print(Book2.publisher)
print(Book2.year)
print(Book2.genre)
print(Book2.pages)
print(Book2.isbn)

print(Book3.title)
print(Book3.author)
print(Book3.publisher)
print(Book3.year)
print(Book3.genre)
print(Book3.pages)
print(Book3.isbn)

print(Book4.title)
print(Book4.author)
print(Book4.publisher)
print(Book4.year)
print(Book4.genre)
print(Book4.pages)
print(Book4.isbn)

class House:
    def __init__(self,address,num_bedrooms,num_bathrooms,square_footage,year_built,price,owner):
        self.address = address
        self.num_bedrooms = num_bedrooms
        self.num_bathrooms = num_bathrooms
        self.square_footage = square_footage
        self.year_built = year_built
        self.price = price
        self.owner = owner

House1 = House("Kira", 4, 2, 1800, 2021, 450000000, "Mustafa Ssebaale")
House2 = House("Namugongo", 3, 3, 1500, 2023, 38000000, "Simeon Bagenda")
House3 = House("Kansanga", 5, 3, 2000, 2022, 40000000, "Opolot Emmanuel" )
House4 = House("Naguru", 8, 9, 5000, 2023, 20000000000, "Melissa Mpenzi")

print(House1.address)
print(House1.num_bedrooms)
print(House1.num_bathrooms)
print(House1.square_footage)
print(House1.year_built)
print(House1.price)
print(House1.owner)

print(House2.address)
print(House2.num_bedrooms)
print(House2.num_bathrooms)
print(House2.square_footage)
print(House2.year_built)
print(House2.price)
print(House2.owner)

print(House3.address)
print(House3.num_bedrooms)
print(House3.num_bathrooms)
print(House3.square_footage)
print(House3.year_built)
print(House3.price)
print(House3.owner)

print(House4.address)
print(House4.num_bedrooms)
print(House4.num_bathrooms)
print(House4.square_footage)
print(House4.year_built)
print(House4.price)
print(House4.owner)


class Cartoon:
    def __init__(self,title,channel,time,rating,age_limit,year_of_release,executive_producer):
        self.title = title
        self.channel = channel
        self.time = time
        self.rating = rating
        self.age_limit = age_limit
        self.year_of_release = year_of_release
        self.executive_producer = executive_producer

Cartoon1 = Cartoon("Fancy Nancy", "Disney Junior" ,"10:30am-11:30am", 3.4, 5, 2018, "Jamie Mitchell Krista Tucker")
Cartoon2 = Cartoon("Spongebob square pants", "Nickelodeon", "9:00am & 7:00pm", "8.2/10", "PG-13", 1999, "Stephen Hillenburg")
Cartoon3 = Cartoon("Thomas & Friends", "Jimjam", "7:00am & 8:00pm", "6.5/10", "2 & above", 2017, "Britt Allcroft")
Cartoon4 = Cartoon("Frozen", "Disney", "11:00am", "6.8/10", "PG", 2013, "John Lasseter")

print(Cartoon1.title)
print(Cartoon1.channel)
print(Cartoon1.time)
print(Cartoon1.rating)
print(Cartoon1.age_limit)
print(Cartoon1.year_of_release)
print(Cartoon1.executive_producer)

print(Cartoon2.title)
print(Cartoon2.channel)
print(Cartoon2.time)
print(Cartoon2.rating)
print(Cartoon2.age_limit)
print(Cartoon2.year_of_release)
print(Cartoon2.executive_producer)

print(Cartoon3.title)
print(Cartoon3.channel)
print(Cartoon3.time)
print(Cartoon3.rating)
print(Cartoon3.age_limit)
print(Cartoon3.year_of_release)
print(Cartoon3.executive_producer)

print(Cartoon4.title)
print(Cartoon4.channel)
print(Cartoon4.time)
print(Cartoon4.rating)
print(Cartoon4.age_limit)
print(Cartoon4.year_of_release)
print(Cartoon4.executive_producer)


class Hotel:
    def __init__(self,name,location,rating,num_rooms,amenities,manager,contact):
        self.name = name
        self.location = location
        self.rating = rating
        self.num_rooms = num_rooms
        self.amenities = amenities
        self.manager = manager
        self.contact = contact

Hotel1 = Hotel("Kampala Serena Hotel", "Nakasero", "5 star", 139, "Water, electricity,wifi", "Anthony Chege", "031 2309000-Tel")
Hotel2 = Hotel("Sheraton Kampala Hotel", "Ternan avenue Kampala", "5 star", 233, "Water, electricity & wifi", "Jean- Phillipe Bittencourt", "031 2322499-Tel")
Hotel3 = Hotel("Speke Resort", "Wavamunno road, Kampala", "4 star", 335, "Water, electricity & wifi", "Kamal Sharma", "041 4227111-Tel")
Hotel4 = Hotel("Grand Imperial Hotel", "Colville St, Kampala", "3 star", 103, "Water and electricity", "Sarah Hirji", "041 4311048-Tel")

print(Hotel1.name)
print(Hotel1.location)
print(Hotel1.rating)
print(Hotel1.num_rooms)
print(Hotel1.amenities)
print(Hotel1.manager)
print(Hotel1.contact)

print(Hotel2.name)
print(Hotel2.location)
print(Hotel2.rating)
print(Hotel2.num_rooms)
print(Hotel2.amenities)
print(Hotel2.manager)
print(Hotel2.contact)

print(Hotel3.name)
print(Hotel3.location)
print(Hotel3.rating)
print(Hotel3.num_rooms)
print(Hotel3.amenities)
print(Hotel3.manager)
print(Hotel3.contact)

print(Hotel4.name)
print(Hotel4.location)
print(Hotel4.rating)
print(Hotel4.num_rooms)
print(Hotel4.amenities)
print(Hotel4.manager)
print(Hotel4.contact)


class Order:
    def __init__(self,order_date,customer_name,product,quantity,delivery_date,status,order_id):
        self.order_date = order_date
        self.customer_name = customer_name
        self.product = product
        self.quantity = quantity
        self.delivery_date = delivery_date
        self.status = status
        self.order_id = order_id

Order1 = Order(2/7/2024, "Michelle", "Wheat", "25kgs", "3/7/2024", "Paid", "XK45J")
Order2 = Order(3/7/2024, "Raphael", "Rice", "200kgs", "3/7/2024", "Paid", "Xa7mo")
Order3 = Order(7/7/2024, "Eleanor", "Cow peas", "10kgs", "8/7/2024", "Paid", "XGY5S")
Order4 = Order(15/7/2024, "David", "Green beans", "100kgs", "17/7/2024", "Credit", "XDC1Q")

print(Order1.order_date)
print(Order1.customer_name)
print(Order1.product)
print(Order1.quantity)
print(Order1.delivery_date)
print(Order1.status)
print(Order1.order_id)

print(Order2.order_date)
print(Order2.customer_name)
print(Order2.product)
print(Order2.quantity)
print(Order2.delivery_date)
print(Order2.status)
print(Order2.order_id)

print(Order3.order_date)
print(Order3.customer_name)
print(Order3.product)
print(Order3.quantity)
print(Order3.delivery_date)
print(Order3.status)
print(Order3.order_id)

print(Order4.order_date)
print(Order4.customer_name)
print(Order4.product)
print(Order4.quantity)
print(Order4.delivery_date)
print(Order4.status)
print(Order4.order_id)


class Student:
    def __init__(self,student_id,name,age,course,gpa,citizenship,contact):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.course = course
        self.gpa = gpa
        self.citizenship = citizenship
        self.contact = contact

Student1 = Student(7233568, "Jean Spencer", 20, "Bachelor of Arts in Development Economics", 2.88, "Canadian", "jspence@gmail.com")
Student2 = Student(7259121, "Roman Rubangakene", 19, "Bachelor of Journalism & Mass communication,", 3.21, "Ugandan", "romanru@gmail,com")
Student3 = Student(7248991, "Emmanuelle Mbithi", 21, "Bachelor in Arts and Design", 3.5, "Kenyan", "emanuellembithi2@gmail.com")
Student4 = Student(7266142, "Daniel Igwe", 23, "Bachelor Of Science in Software Engineering", 3.2, "Nigerian", "igwedanny@gmail.com")

print(Student1.student_id)
print(Student1.name)
print(Student1.age)
print(Student1.course)
print(Student1.gpa)
print(Student1.citizenship)
print(Student1.contact)

print(Student2.student_id)
print(Student2.name)
print(Student2.age)
print(Student2.course)
print(Student2.gpa)
print(Student2.citizenship)
print(Student2.contact)

print(Student3.student_id)
print(Student3.name)
print(Student3.age)
print(Student3.course)
print(Student3.gpa)
print(Student3.citizenship)
print(Student3.contact)

print(Student4.student_id)
print(Student4.name)
print(Student4.age)
print(Student4.course)
print(Student4.gpa)
print(Student4.citizenship)
print(Student4.contact)


class Movie:
    def __init__(self,title,director,release_year,genre,duration,main_cast,rating):
        self.title = title
        self.director = director
        self.release_year = release_year
        self.genre = genre
        self.duration = duration
        self.main_cast = main_cast
        self.rating = rating

Movie1 = Movie("Acrimony", "Tyler Perry", 2018, "Psychological thriller","2:00 hours", "Taraji P Henson", 4.4)
Movie2 = Movie("The Idea Of You", "Michael Showalter", 2024, "Romantic Comedy", "1:55 hours", "Anne Hathaway & Nicholas Galitzine", 4.3)
Movie3 = Movie("Fast $ Furious 5", "Justin Lin", 2011, "Action", "2:11 hours", "Paul Walker & Elsa Pataky", 4.6)
Movie4 = Movie("Interstellar", "Christopher Nolan", 2014, "Science Fiction", "2:49hours", "Matthew  McConaughey, Anne Hathaway & Jessica Chastain", 8.7)

print(Movie1.title)
print(Movie1.director)
print(Movie1.release_year)
print(Movie1.genre)
print(Movie1.duration)
print(Movie1.main_cast)
print(Movie1.rating)

print(Movie2.title)
print(Movie2.director)
print(Movie2.release_year)
print(Movie2.genre)
print(Movie2.duration)
print(Movie2.main_cast)
print(Movie2.rating)

print(Movie3.title)
print(Movie3.director)
print(Movie3.release_year)
print(Movie3.genre)
print(Movie3.duration)
print(Movie3.main_cast)
print(Movie3.rating)

print(Movie4.title)
print(Movie4.director)
print(Movie4.release_year)
print(Movie4.genre)
print(Movie4.duration)
print(Movie4.main_cast)
print(Movie4.rating)

#THE END.

        

        