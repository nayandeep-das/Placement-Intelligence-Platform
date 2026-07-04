CREATE DATABASE placement_platform;

USE placement_platform;

CREATE TABLE Branches (
    BranchID INT AUTO_INCREMENT PRIMARY KEY,
    BranchCode VARCHAR(10) NOT NULL UNIQUE,
    BranchName VARCHAR(100) NOT NULL,
    BranchType ENUM('Core', 'Non-Core', 'Core+Non-Core', 'Research') NOT NULL
);

INSERT INTO Branches (BranchCode, BranchName, BranchType)
VALUES
('CSE','Computer Science and Engineering','Non-Core'),
('ECE','Electronics and Communication Engineering','Core+Non-Core'),
('EE','Electrical Engineering','Core'),
('ME','Mechanical Engineering','Core'),
('CE','Civil Engineering','Core'),
('CHE','Chemical Engineering','Core'),
('MME','Metallurgical and Materials Engineering','Core'),
('BT','Biotechnology','Research');

SELECT * FROM Branches;

CREATE TABLE Roles (
    RoleID INT AUTO_INCREMENT PRIMARY KEY,
    RoleName VARCHAR(100) NOT NULL,
    RoleType ENUM('Software','Core','Analytics','Finance','Research','Consulting') NOT NULL
);

INSERT INTO Roles (RoleName, RoleType)
VALUES
('Software Engineer','Software'),
('Backend Developer','Software'),
('Frontend Developer','Software'),
('Full Stack Developer','Software'),
('Data Analyst','Analytics'),
('Machine Learning Engineer','Analytics'),
('Embedded Engineer','Core'),
('Electrical Engineer','Core'),
('Mechanical Engineer','Core'),
('Civil Engineer','Core'),
('Process Engineer','Core'),
('Metallurgical Engineer','Core'),
('Research Associate','Research'),
('Technology Consultant','Consulting'),
('Business Analyst','Consulting');

SELECT * FROM Roles;

CREATE TABLE Skills (
    SkillID INT AUTO_INCREMENT PRIMARY KEY,
    SkillName VARCHAR(100) UNIQUE NOT NULL,
    DifficultyWeight INT NOT NULL CHECK (DifficultyWeight BETWEEN 1 AND 5)
);

INSERT INTO Skills (SkillName, DifficultyWeight)
VALUES
('Python',4),
('Java',4),
('C',4),
('C++',4),
('SQL',3),
('DSA',5),
('OOP',4),
('DBMS',4),
('Operating Systems',4),
('Computer Networks',4),
('Git',2),
('Linux',3),
('Pandas',3),
('NumPy',3),
('Scikit-Learn',4),
('Power BI',3),
('Excel',2),
('MATLAB',4),
('Embedded Systems',5),
('Verilog',5),
('PLC',5),
('Power Systems',5),
('AutoCAD',4),
('SolidWorks',4),
('STAAD Pro',4),
('Surveying',3),
('Aspen Plus',5),
('Thermodynamics',4),
('Metallurgy',5),
('Materials Science',4),
('PCR',5),
('Cell Culture',5),
('Molecular Biology',5);

SELECT * FROM Skills;

CREATE TABLE Placements (

    PlacementID INT AUTO_INCREMENT PRIMARY KEY,

    StudentID INT NOT NULL,

    CompanyRoleID INT NOT NULL,

    PlacementStatus ENUM('Placed','Not Placed') NOT NULL,

    PlacementDate DATE,

    FOREIGN KEY (StudentID)
        REFERENCES Students(StudentID),

    FOREIGN KEY (CompanyRoleID)
        REFERENCES CompanyRoles(CompanyRoleID)
);