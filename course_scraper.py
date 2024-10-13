import requests
from bs4 import BeautifulSoup

def fetch_top_courses(url):
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to retrieve data: {response.status_code}")
        return []

    soup = BeautifulSoup(response.content, 'html.parser')
    course_elements = soup.find_all('div', class_='course-card')  # Example class name
    
    courses = []
    for course_element in course_elements:
        title = course_element.find('h2').get_text(strip=True)
        rating = float(course_element.find('span', class_='course-rating').get_text(strip=True))
        students = int(course_element.find('span', class_='course-students').get_text(strip=True).replace(',', ''))
        
        courses.append({
            'title': title,
            'rating': rating,
            'students': students
        })
    
    # Sort courses based on rating and number of students
    courses.sort(key=lambda x: (x['rating'], x['students']), reverse=True)
    
    return courses[:3]  # Return top 3 courses

# Example usage
if __name__ == "__main__":
   input(role)
    url = 'https://www.google.com/search?q=top+courses+for+f(role)&oq=top+courses+for+(role)&gs_lcrp=EgZjaHJvbWUqCQgBECEYChigATIGCAAQRRg5MgkIARAhGAoYoAEyBwgCECEYnwUyBwgDECEYnwUyBwgEECEYnwXSAQkxODE2MWowajeoAgCwAgA&sourceid=chrome&ie=UTF-8'  # Replace with the actual URL
    top_courses = fetch_top_courses(url)
    for course in top_courses:
        print(f"Title: {course['title']}")
        print(f"Rating: {course['rating']}")
        print(f"Students: {course['students']}\n")
