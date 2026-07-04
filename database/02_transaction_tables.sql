USE placement_platform;

CREATE TABLE Students (
    StudentID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Gender ENUM('Male','Female') NOT NULL,
    Email VARCHAR(100) UNIQUE,
    Phone VARCHAR(15),
    BranchID INT NOT NULL,
    CGPA DECIMAL(3,2) NOT NULL,
    DSASolved INT DEFAULT 0,
    Projects INT DEFAULT 0,
    Internships INT DEFAULT 0,
    CommunicationScore INT,
    AptitudeScore INT,
    PreferredRoleID INT,
    PlacementStatus ENUM('Placed','Not Placed') DEFAULT 'Not Placed',

    FOREIGN KEY (BranchID) REFERENCES Branches(BranchID),
    FOREIGN KEY (PreferredRoleID) REFERENCES Roles(RoleID)
);

CREATE TABLE Companies (
    CompanyID INT AUTO_INCREMENT PRIMARY KEY,
    CompanyName VARCHAR(100) NOT NULL UNIQUE,
    Category ENUM('Category-1','Category-2','Category-3') NOT NULL,
    Industry VARCHAR(100),
    Headquarters VARCHAR(100)
);

CREATE TABLE CompanyRoles (
    CompanyRoleID INT AUTO_INCREMENT PRIMARY KEY,
    CompanyID INT NOT NULL,
    RoleID INT NOT NULL,
    Package DECIMAL(5,2),
    FOREIGN KEY (CompanyID) REFERENCES Companies(CompanyID),
    FOREIGN KEY (RoleID) REFERENCES Roles(RoleID)
);

CREATE TABLE StudentSkills (
    StudentID INT,
    SkillID INT,
    PRIMARY KEY (StudentID, SkillID),

    FOREIGN KEY (StudentID) REFERENCES Students(StudentID),
    FOREIGN KEY (SkillID) REFERENCES Skills(SkillID)
);

CREATE TABLE RoleSkills (
    RoleID INT,
    SkillID INT,
    PRIMARY KEY(RoleID, SkillID),

    FOREIGN KEY(RoleID) REFERENCES Roles(RoleID),
    FOREIGN KEY(SkillID) REFERENCES Skills(SkillID)
);

CREATE TABLE CompanyEligibility (
    CompanyRoleID INT,
    BranchID INT,
    MinimumCGPA DECIMAL(3,2),

    PRIMARY KEY(CompanyRoleID, BranchID),

    FOREIGN KEY(CompanyRoleID) REFERENCES CompanyRoles(CompanyRoleID),
    FOREIGN KEY(BranchID) REFERENCES Branches(BranchID)
);

CREATE TABLE Placements (
    PlacementID INT AUTO_INCREMENT PRIMARY KEY,
    StudentID INT NOT NULL,
    CompanyRoleID INT NOT NULL,
    PlacementDate DATE,
    OfferStatus ENUM('Offered','Rejected','Accepted'),
    JoiningStatus ENUM('Joined','Not Joined','Pending'),

    FOREIGN KEY(StudentID) REFERENCES Students(StudentID),
    FOREIGN KEY(CompanyRoleID) REFERENCES CompanyRoles(CompanyRoleID)
);

SHOW TABLES;