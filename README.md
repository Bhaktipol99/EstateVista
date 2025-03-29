**WHAT IS ESTATEVISTA??**
 EstateVista is a real estate management system
 designed to facilitate property transactions, rental
 management, and customer engagement. The
 platform provides users with seamless property listing,
 booking, and management functionalities.
 Scope:
 EstateVista allows users to list, view, and search for properties based on
 location, price, and features. It provides secure authentication, user
 dashboards, and an efficient property filtering mechanism. The system
 does not involve agents, focusing solely on direct user interactions.
 
**PURPOSE**
 The primary objective of EstateVista is to create a
 user-friendly, efficient, and transparent platform for
 property management. Users can register, list
 properties, search for suitable properties, and directly
 communicate with property owners. The system
 eliminates intermediaries, ensuring a cost-effective
 and streamlined approach to real estate
 transactions.
 
**OBJECTIVES**
 EstateVista aims to provide an efficient and user-friendly platform for
 property management, enabling seamless interaction between
 buyers and sellers. The key objectives include:
 Simplifying the property listing and searching process.
 Providing detailed property insights with images and specifications.
 Ensuring secure and smooth transactions.
 Enhancing the user experience through an intuitive interface.
 Implementing robust authentication and data security measures.
User Type Role Main Actions
 Buyer Property Seeker
 Browse property listings, inquire
 about properties, schedule visits,
 and purchase/rent properties.
 Seller Property Owner
 List properties for sale/rent, set
 prices, manage property details,
 and respond to buyer inquiries.
 Admin Platform Manager
 Manage users, verify property
 listings, handle transactions, and
 maintain system security.
 
 **REQUIREMENT GATHERING**
**FESIBILITY STUDY****
 Technical Feasibility:
 EstateVista integrates modern web technologies such as HTML, CSS, JavaScript, Python, and
 SQLite to ensure a seamless and scalable platform. These technologies are widely used and
 compatible, making implementation and maintenance efficient.
 
 Operational Feasibility:
 The platform is designed to be user-friendly and intuitive, alowing buyers and selers to
 navigate effortlessly. A feedback system enables continuous improvement by gathering user insights,
 ensuring a smooth and satisfactory experience.
 
 Time Feasibility:
 EstateVista saves time by centralizing property listings, reducing the need for users to browse
 multiple platforms. Efficient search and filtering options alow users to find relevant listings quickly,
 enhancing convenience.
 Behavioral Feasibility:
 The platform is designed for ease of use, encouraging adoption among buyers and selers. Its
 simple        
interface, clear processes, and responsive design make it accessible to a wide audience,
 ensuring a positive user experience.
 
**FUNCTIONAL REQUIREMENT**
 User Authentication: Users must register and log in to access certain
 features.
 Property Listing: Sellers can list their properties with details such as
 price, location, images, and description.
 Search & Filter: Buyers can search for properties using various filters
 like price, location, and property type.
 Direct Communication: The system allows direct messaging between
 buyers and sellers.
 Favorites & Shortlist: Users can save properties they are interested in
 for future reference.
 Admin Panel: Admins can manage user accounts, monitor property
 listings, and handle reported issues.
 
**NON FUNCTIONAL REQUIREMENT**
 Scalability: The system should be able to handle an increasing number of users
 and property listings.
 Security: Secure authentication, data encryption, and fraud prevention
 mechanisms must be implemented.
 Performance: Pages should load efficiently, and the search function should
 return results within seconds.
 User-Friendly Interface: The UI should be intuitive and accessible for all users,
 including non-tech-savvy individuals.
 Reliability: The system should have minimal downtime and ensure smooth
 functionality.
**SYSTEM REQUIREMENTS**
 Hardware Requirements (Local Development)
 System Requirements: Minimum 4GB RAM, Dual-Core Processor
 Storage: Local storage (at least 10GB free space for media files)
 Database: Django’s inbuilt SQLite database
 ⚙
 Software Requirements
 Backend: Django (Python)
 Frontend: HTML, CSS, JavaScript
 Database: SQLite (default Django database)
 Version Control: GitHub (for project tracking)
 Local Server: Django’s built-in development server (runserver)
 
**SYSTEM DESIGN & ARCHITECTURE**
 MVT (MODEL-VIEW-TEMPLATE) STRUCTURE IN DJANGO
 Models → User, Property, Category, Inquiry,
 Review, Message, Payment
 Views → CRUD for properties (List, Detail, Create,
 Update, Delete)
 Templates → Buyer & Seller UI (Browse, Manage
 Listings). 
 
**FUTURE ENHANCEMENT**
 AI-based property recommendations
 3D virtual tours
 Smart filters
 Chatbot support
 Mortgage calculator
 Legal verification
 Real-time analytics

**CONCLUSION****
 EstateVista aims to be a leading platform for seamless
 property buying, selling, and renting. It enhances user
 experience with AI-driven recommendations, virtual
 tours, and smart filters, serving as a one-stop solution
 for buyers, sellers, and real estate professionals.
