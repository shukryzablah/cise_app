if __name__ == "__main__":
    code_num = 27.0102
    names = ['Algebra and Number Theory',
            'Analysis and Functional Analysis',
            'Applied Mathematics',
            'Computational and Applied Mathematics',
            'Computational Mathematics',
            'Financial Mathematics',
            'Geometry/Geometric Analysis',
            'Mathematical Biology',
            'Mathematical Statistics and Probability',
            'Mathematics and Statistics',
            'Mathematics',
            'Statistics',
            'Topology and Foundations']
    
    majors = []
    for i in range(len(names)):
        major = Major(cip_code=str(code_num)[:6], name=names[i], abbreviation=names[i][:3])
        db.session.add(major)
        majors.append(major)
        code_num = code_num + .001
        
    

