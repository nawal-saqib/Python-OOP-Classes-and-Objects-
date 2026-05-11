# Problem 1
class Book:
    file_path = "C:/Users/HP/Documents/book.txt"
    def __init__(self, price = 0, author = "", publishing_year = 0):
        self.price = price
        self.author = author
        self.publishing_year = publishing_year
    def add_book(self):
        try:
            add_price = int(input("Please enter the price of the book."))
            add_publishing_year = int(input("Please enter the publishing year."))
            add_author = input("Please enter the name of the author")
            file = open(Book.file_path, "a")
            file.writelines(str(add_price) + ", " + add_author + ", " + str(add_publishing_year) + "\n")
            file.close()
        except ValueError:
            print("Please enter an integer.")
    def display_book_information(self):
        try:
            file = open(Book.file_path, "r")
            books = file.readlines()
            if not books:
                print("No books are stored.")
            else:
                for i in books:
                    print(i)
            file.close()
        except FileNotFoundError:
            print("The file was not found.")
    def books_of_author(self):
        try:
            same_author_book = []
            enter_author = input("Please enter the name of the author you want to find the books of.")
            file = open(Book.file_path, "r")
            book_list = file.readlines()
            for lines in book_list:
                price, author, publishing_year = lines.strip().split(", ")
                if author.lower() == enter_author.lower():
                    same_author_book.append(price + "  " + author + "  " + publishing_year)
            if same_author_book:
                    print("Books by the author: ")
                    for book in same_author_book:
                        print(book)
            else:
                print("No book by the same author was found.")
            file.close()
        except FileNotFoundError:
            print("This file does not exist.")
    def book_prices(self):
        try:
            prices = []
            file = open(Book.file_path, "r")
            book_list = file.readlines()
            for lines in book_list:
                price, author, publishing_year = lines.strip().split(", ")
                prices.append(int(price))
            if prices:
                total_price = sum(prices)
                average_price = total_price / len(prices)
                maximum_price = max(prices)
                minimum_price = min(prices)
                print("Total price: " + str(total_price))
                print("Average price: " + str(average_price))
                print("Maximum price: " + str(maximum_price))
                print("Minimum price: " + str(minimum_price))
            else:
                print("No books are stored.")
            file.close()
        except FileNotFoundError:
            print("The file was not found.")
def main():
    new_book = Book()
    while True:
        print("Library Management System.")
        print("1. Add book information.")
        print("2. Display book information.")
        print("3. List all books of given author.")
        print("4. Return the sum, average, maximum and minimum of book prices.")
        print("5. Exit")  
        choice = input("Enter your choice: ")
        if choice == '1':
            new_book.add_book()
        elif choice == '2':
            new_book.display_book_information()
        elif choice == '3':
            new_book.books_of_author()
        elif choice == '4':
            new_book.book_prices()
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid. Please enter a number from 1 to 5.")
main()

# Problem 2
def RLE(string):
    if string == "":
        return ""
    now_letter = string[0]
    count = 1
    for i in range(1, len(string)):
        if string[i] == now_letter:
            count += 1
        else:
            if count > 1:
                result = now_letter + str(count)
            else:
                result = now_letter
            return result + RLE(string[i:])
    if count > 1:
        return now_letter + str(count)
    else:
        return now_letter
print(RLE("aaaabccddddde"))  
print(RLE("ab"))              
print(RLE("a"))               
print(RLE("aaa"))             
print(RLE(""))                

# Problem 3
# part a
def addition(lst):
    total = 0
    for i in lst:
        if type(i) == type([]):
            total = total + addition(i)
        else:
            total = total + i
    return total
print(addition([1, 2, [3, 4], [5, 6]]))

# part b
def double(string):
    if string == "":
        return ""
    else:
        return string[0] * 2 + double(string[1 : ])
print(double("apple"))

# Problem 4
class KFC:
    _total_sales = 0
    def __init__(self, branch_name, employees, branch_sales  = 0, sold_meals = 0):
        self._branch_name = branch_name
        self._employees = employees
        self._branch_sales = branch_sales
        self._sold_meals = sold_meals
    def sale(self, number_of_meals, price_per_meal):
        sales_total_amount = number_of_meals * price_per_meal
        self._branch_sales += sales_total_amount
        self._sold_meals += number_of_meals
        KFC._total_sales += sales_total_amount
    def get_branch_sales(self):
        return self._branch_sales
    def get_total_sales(self):
        return KFC._total_sales
    def get_employees(self):
        print(self._employees)
def main():
    branch1 = KFC("Lahore", ["Ali", "Ayesha", "Shahzad"])
    branch2 = KFC("Karachi", ["Sara", "Naveed", "Ahmed"])
    branch3 = KFC("Peshawar", ["Amna", "Hussain", "Waleed"])
    branch1.sale(70, 10)
    branch2.sale(120, 6)
    branch3.sale(65, 8)
    print(branch1._branch_name + " has " + str(branch1.get_branch_sales()) + "number of sales.")
    print(branch2._branch_name + " has " + str(branch2.get_branch_sales()) + "number of sales.")
    print(branch3._branch_name + " has " + str(branch3.get_branch_sales()) + "number of sales.")
    print("Total Sales: " + str(branch1.get_total_sales()))
    branch1.get_employees()
    branch2.get_employees()
    branch3.get_employees()
main()

# Problem 5
class Song:
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration
    def get_duration(self):
        return self.duration
    def display_song(self):
        print("Song name: " + self.title + " and Duration: " + str(self.duration))
class Album:
    def __init__(self, title, year):
        self.title = title
        self.year = year
        self.songs = [] 
    def add_song(self, new_song_title, new_song_duration):
        song = Song(new_song_title, new_song_duration)
        self.songs.append(song)
    def get_album_title(self):
        return self.title
    def display_songs(self):
        for song in self.songs:
            song.display_song()
    def display_album(self):
        print("Album title: " + self.title + "Year: " + self.year)
        self.display_songs()
class Artist:
    def __init__(self, name):
        self.name = name
        self.albums = []  
    def get_artist_name(self):
        return self.name
    def add_album(self, album):
        self.albums.append(album)
    def get_album(self, album_title):
        for album in self.albums:
            if album.title == album_title:
                return album
        return None
    def display_albums(self):
        for album in self.albums:
            album.display_album() 
    def display_artist(self):
        print("Artist name: " + self.name)
        self.display_albums()
class MusicLibrary:
    file_path = "C:/Users/HP/Documents/Music_Library.txt"
    def __init__(self):
        self.artists = [] 
    def add_artist(self, artist):
        self.artists.append(artist)
    def display_artists(self):
        for artist in self.artists:
             artist.display_artist()
    def get_artist(self, name):
        for artist in self.artists:
            if artist.name == name:
                return artist
        return None
    def file_handling(self):
        file = open(MusicLibrary.file_path, "r")
        for line in file:
            artist_name, album_title, year, song_title, duration = line.strip().split(", ")
            duration = int(duration)
            artist = self.get_artist(artist_name)
            if not artist:
                artist = Artist(artist_name)
                self.add_artist(artist)
            album = artist.get_album(album_title)
            if not album:
                album = Album(album_title, year)
                artist.add_album(album)
            album.add_song(song_title, duration)
        file.close()
def main():
    library = MusicLibrary()
    library.file_handling()
    print("Artists in the Music Library:")
    library.display_artists()
    artist_name = "Alan Walker"  
    artist = library.get_artist(artist_name)
    if artist:
        print("Albums by " + artist_name)
        artist.display_albums()       
        for album in artist.albums:
            print("Songs in album: " + album.get_album_title())
            album.display_songs()
    else:
        print("The artist " + artist_name +  " was not found in the library.")
main()

# Problem 6
class Department:
    def __init__(self, name):
        self.name = name
        self.courses = []
        self.students = []
    def add_course(self, course):
        self.courses.append(course)
        course.add_department(self)
    def add_student(self, student):
        self.students.append(student)
        student.add_department(self)
class Course:
    def __init__(self, name):
        self.name = name
        self.departments = []
    def add_department(self, department):
        if department not in self.departments:
            self.departments.append(department)
class Student:
    def __init__(self, name):
        self.name = name
        self.courses = []
        self.departments = []
    def add_course(self, course):
        self.courses.append(course)
        if course not in self.departments:
            for department in course.departments:
                self.add_department(department)
    def add_department(self, department):
        if department not in self.departments:
            self.departments.append(department)
            department.add_student(self)
def main():
    department1 = Department("Computer Science")
    department2 = Department("Business")
    courses = [Course("Course1"), Course("Course2"), Course("Course3"), Course("Course4"), Course("Course5"), Course("Course6"), Course("Course7"), Course("Course8"), Course("Course9"), Course("Course10"), Course("Course11"), Course("Course12"), Course("Course13"), Course("Course14"), Course("Course15"), Course("Course16"), Course("Course17"), Course("Course18"), Course("Course19"), Course("Course20")]
    students = [Student("Student1"), Student("Student2"), Student("Student3"), Student("Student4"), Student("Student5"), Student("Student6"), Student("Student7"), Student("Student8"), Student("Student9"), Student("Student10")]
    for i in range(len(courses)):
        if i % 2 == 0:
            department1.add_course(courses[i])
        else:
            department2.add_course(courses[i])
    for i in range(len(students)):
        students[i].add_course(courses[i % 20])
        students[i].add_course(courses[(i + 1) % 20])
    print("Departments and their students:")
    for dept in [department1, department2]:
        print(dept.name) 
        for student in dept.students:
            courses_enrolled = []
            for course in student.courses:
                courses_enrolled.append(course.name)
            print("  - " + student.name + " enrolled in: " + ', ' .join(courses_enrolled))
    print("\nCourses and their departments:")
    for course in courses:
        departments_names = ', '.join(dept.name for dept in course.departments)
        print(course.name + " belongs to: " + departments_names)
main()


        
        


