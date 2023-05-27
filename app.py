import streamlit as st

def main():
    #---- mengatur lebar tampilan -----
    st.markdown('<style>body{max-width: 800px; margin: auto;}</style>', unsafe_allow_html=True)
    


# Judul halaman
    st.title("📝 Resume")

    # Menambahkan foto profil
    profile_pic = "./images/pas.jpg"
    st.image(profile_pic, caption='Foto Profil', use_column_width=False, output_format='JPG', width=150,)

    # Informasi pribadi
    st.header("About Me :wave:")
    st.write("As a versatile data professional, I specialize in data science, data analysis, data engineering and front-end development. With expertise in Python, R, SQL, Power BI, Tableau, Excel, Spark, SQL, machine learning, JavaScript, React, HTML, CSS, Golang, I am well-equipped to deliver powerful insights and solutions across various domains.")
    st.write("I hold a degree in Metallurgical Engineering from the Sultan Ageng Tirtayasa. Over the past years, I have completed numerous training programs focused on honing my data science skills and have contributed to several data-related projects.")
    st.write("I am passionate about using data to inform decision-making and solve complex business challenges. I thrive in fast-paced, collaborative environments and am always looking for new opportunities to learn and grow in my field.")
    
    st.header("Personal Infromation")
    st.subheader(":male-office-worker: Nama")
    st.write("Aditya Nur Ilman Wibowo")
    st.subheader("🏠 Alamat")
    st.write("Ramanuju Baru RT 02/09 No 42, Citangkil, Cilegon, Banten")
    st.subheader("📧 Email")
    st.write("adityanurilmanw@gmail.com")
    st.subheader(":iphone: Telepon")
    st.write("+6287770854496")

    # Pendidikan
    st.header("🎓 Education")
    st.subheader("🎓 Bachelor of Metallurgical Engineering")
    st.write("Sultan Ageng Tirtayasa University (2016 - 2021)")
    
    # Pengalaman Kerja
    st.header("💼 Experience")
    st.subheader("Supervisor Logistic")
    st.write("Mega Persada Group, 2021 - 2022")
    st.write("Descriptiom")
    st.write("Responsible for logistic supply chain operational (3 Companies under Mega Persada Group), logistic KPI achievement and analysis and logistic improvement process. Managed transportation supply chain National Distribution Center (NDC) to Indirect Distribution Center (IDC) and Distribution Center (DC). Maintain 3PL performance, fullfillment partners, complaint handling improvement and return rate. Develop data management systems and database for logistic process improvement and cost saving initiative. Operated more than 30 internal carriers, 20-30 containers per month, and lead more than 30 peoples. Succeed in increase 30% the KPI Truck Utilization Rate with optimization data trucking ")
    st.write(" Relevant Work Experience : Data Analyst, Big Data, SQL, Tablue, Web Daskboard ")
    
    # Skills
    st.header("🔧 Skills")
    st.subheader("🐍 Programming Language")
    st.write("- Python")
    st.write("- JavaScript")
    st.subheader("🌐 Web Development")
    st.write("- HTML/CSS")
    st.write("- Golang")
    st.write("- React")


if __name__ == '__main__':
    main()
