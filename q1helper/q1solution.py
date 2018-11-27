from collections import defaultdict
from math import sqrt,atan2


def integrate(f : callable, n : int) -> callable:
    if type(n) is not int or n <= 0:
        raise AssertionError("Variable n was not an integer > 0")
    def approx_int(a: float, b: float) -> float:
        if not a <= b:
            raise AssertionError("Bounds were not valid (a must be <= b)")
        dx = (b-a)/n
        integral = 0.0
        for i in range(0,n):
            integral += f(a+i*dx)*dx
        return integral
    return approx_int



def sorted1 (ps : {int:(int,int)}) -> [(int,(int,int))]:
    return [(ordinal,(ps[ordinal])) for ordinal in sorted(ps, key=(lambda k: ps[k]))]



def sorted2 (ps : {int:(int,int)}) -> [(int,int)]:
    return [point for point in sorted(ps.values(), key=(lambda k: atan2(k[1],k[0])), reverse=True)]



def sorted3 (ps : {int:(int,int)}) -> [int]:
    return [ordinal for ordinal in sorted(ps, key=(lambda k: sqrt((ps[k][0]**2)+(ps[k][1]**2))))]



def points (ps : {int:(int,int)}) -> [(int,int)]:
    return [ps[ordinal] for ordinal in sorted(ps)]



def first_quad (ps : {int:(int,int)}) -> {(int,int):float}:
    return {point: (sqrt(point[0]**2+point[1]**2)) for point in ps.values() if point[0] >= 0 and point[1] >= 0}



def movie_rank(db : {str:{(str,int)}}) -> [(str,float)]:
    rank_list = []
    for movie in db:
        rank_sum = 0.0
        for rank in db[movie]:
            rank_sum += rank[1]
        rank_list.append((movie,rank_sum/len(db[movie])))
    return sorted(rank_list, key= lambda k: (-k[1],k[0]))


def reviewer_dict(db : {str:{(str,int)}}) -> {str:{(str,int)}}:
    reviewers = defaultdict(set)
    for aset in db:
        for movie in db[aset]:
            reviewers[movie[0]].add((aset, movie[1]))
    return dict(reviewers)





if __name__ == '__main__':
    # This code is useful for debugging your functions, especially
    #   when they raise exceptions: better than using driver.driver().
    # Feel free to add more tests (including tests showing in the bscF18.txt file)
    # Use the driver.driver() code only after you have removed anybugs
    #   uncovered by these test cases.
    
    print('Testing integrate')
    f = integrate( (lambda x : x), 100)
    print(f(0,1),f(0,2),f(-1,1))
    f = integrate( (lambda x : 3*x**2 - 2*x + 1), 1000)
    print(f(0,1),f(0,2),f(-1,1))
 
 
    print('\nTesting sorted1')
    ps1 = {1:(1,1),2:(3,2),3:(3,-3),4:(-3,4),5:(-2,-2)} 
    ps2 = {1:(0,5), 2:(2,3), 3:(-3,2), 4:(-5,1), 5:(-3,-2), 6:(4,-2), 7:(5,0), 8:(0,-5)}  
    print(sorted1(ps1))
    print(sorted1(ps2))
 
    print('\nTesting sorted2')
    ps1 = {1:(1,1),2:(3,2),3:(3,-3),4:(-3,4),5:(-2,-2)} 
    ps2 = {1:(0,5), 2:(2,3), 3:(-3,2), 4:(-5,1), 5:(-3,-2), 6:(4,-2), 7:(5,0), 8:(0,-5)}  
    print(sorted2(ps1))
    print(sorted2(ps2))
 
    print('\nTesting sorted3')
    ps1 = {1:(1,1),2:(3,2),3:(3,-3),4:(-3,4),5:(-2,-2)} 
    ps2 = {1:(0,5), 2:(2,3), 3:(-3,2), 4:(-5,1), 5:(-3,-2), 6:(4,-2), 7:(5,0), 8:(0,-5)}  
    print(sorted3(ps1))
    print(sorted3(ps2))
    
    print('\nTesting points')
    ps1 = {1:(1,1),2:(3,2),3:(3,-3),4:(-3,4),5:(-2,-2)} 
    ps2 = {1:(0,5), 2:(2,3), 3:(-3,2), 4:(-5,1), 5:(-3,-2), 6:(4,-2), 7:(5,0), 8:(0,-5)}  
    print(points(ps1))
    print(points(ps2))
 
    print('\nTesting first_quad')
    ps1 = {1:(1,1),2:(3,2),3:(3,-3),4:(-3,4),5:(-2,-2)} 
    ps2 = {1:(0,5), 2:(2,3), 3:(-3,2), 4:(-5,1), 5:(-3,-2), 6:(4,-2), 7:(5,0), 8:(0,-5)}  
    print(first_quad(ps1))
    print(first_quad(ps2))
 
    print('\nTesting movie_rank')
    db1 = {'Psycho':  {('Bob',5),  ('Carrie',5), ('Alan', 1), ('Diane', 1), }, 'Amadeus': {('Bob',3),  ('Carrie',3), ('Diane',3)}, 'Up': {('Alan',2), ('Diane',5)} }
    db2 = {'Psycho':  {('Bob',5),  ('Carrie',5), ('Alan', 1), ('Diane', 1), ('Evan',4), ('Fawn',2)},
           'Amadeus': {('Bob',3),  ('Carrie',3), ('Diane',3)},
           'Up': {('Alan',2), ('Diane',5)},
           'Casablaca': {('Alan',2), ('Diane',5), ('Evan',2)},
           'Rashamon': {('Alan',2), ('Diane',5), ('Fawn',3), ('Gary',4)},
           'Alien': {('Alan',2), ('Diane',5), ('Evan',5), ('Fawn',5)}}
    print(movie_rank(db1))
    print(movie_rank(db2))
 
    print('\nTesting reviewer_dict')
    db1 = {'Psycho':  {('Bob',5),  ('Carrie',5), ('Alan', 1), ('Diane', 1)}, 'Amadeus': {('Bob',3),  ('Carrie',3), ('Diane',3)}, 'Up': {('Alan',2), ('Diane',5)} }
    db2 = {'Psycho':  {('Bob',5),  ('Carrie',5), ('Alan', 1), ('Diane', 1), ('Evan',4), ('Fawn',2)},
           'Amadeus': {('Bob',3),  ('Carrie',3), ('Diane',3)},
           'Up': {('Alan',2), ('Diane',5)},
           'Casablaca': {('Alan',2), ('Diane',5), ('Evan',2)},
           'Rashamon': {('Alan',2), ('Diane',5), ('Fawn',3), ('Gary',4)},
           'Alien': {('Alan',2), ('Diane',5), ('Evan',5), ('Fawn',5)}}
    print(reviewer_dict(db1))
    print(reviewer_dict(db2))
 
 
    print('\ndriver testing with batch_self_check:')
    import driver
    driver.default_file_name = "bscq1F18.txt"
    driver.default_show_traceback = True
    driver.default_show_exception = True
    driver.default_show_exception_message = True
    driver.driver()           

