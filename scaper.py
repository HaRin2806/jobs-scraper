import requests
from bs4 import BeautifulSoup
import csv

def scrape_jobs():
    url = "https://realpython.github.io/fake-jobs/"
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f"Loi khi tai trang web")
        return
    soup = BeautifulSoup(response.content, "html.parser")
    job_elements = soup.find_all("div", class_="card-content")
    jobs_data = []
    
    #Trích xuất thông tin
    for job_element in job_elements:
        # Xử lý edge cases (nếu thiếu trường dữ liệu, sẽ trả về 'N/A' thay vì báo lỗi)
        title_elem = job_element.find("h2", class_="title")
        company_elem = job_element.find("h3", class_="company")
        location_elem = job_element.find("p", class_="location")
        
        links = job_element.find_all("a")
        job_url = links[1]["href"] if len(links) > 1 else "N/A"
        # Làm sạch dữ liệu văn bản (loại bỏ khoảng trắng thừa)
        title = title_elem.text.strip() if title_elem else "N/A"
        company = company_elem.text.strip() if company_elem else "N/A"
        location = location_elem.text.strip() if location_elem else "N/A"
        
        jobs_data.append([title, company, location, job_url])
        
    csv_filename = "python_jobs.csv"
    
    # Sử dụng 'utf-8' để tránh lỗi font chữ
    with open(csv_filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        # Ghi dòng tiêu đề
        writer.writerow(["Job Title", "Company Name", "Location", "Job Detail URL"])
        # Ghi toàn bộ dữ liệu
        writer.writerows(jobs_data)

    print(f"Scraping thành công! Đã lưu {len(jobs_data)} công việc vào {csv_filename}")

if __name__ == "__main__":
    scrape_jobs()
        
        
        
    