
    // Initial language setting
    var currentLanguage = 'en';

    // Function to toggle between English and Arabic
    function toggleLanguage() {
        // Toggle the language
        currentLanguage = currentLanguage === 'en' ? 'ar' : 'en';

        // Update content based on the selected language
        updateLanguageContent();
    }

    // Function to update language-specific content
    function updateLanguageContent() {
        if (currentLanguage === 'ar') {
            // Arabic content
            $('#siteTitle').text('عقلية التوحد');
            $('#SiteTheem').text('التوحد ليس إعاقة.');
            $('#aboutus').text('من نحن');
            $('#ABOUT').text('عننا');
            $('#TEAM').text('الفريق');
            $('#OURSERVICES').text('خدماتنا');
            $('#SpecialistCare').text('عناية المختصين');
            $('#community').text('المجتمع');
            $('#contact').text('تواصل');
            $('#LearnMore').text('اعرف أكثر');

            // ... Update other elements ...
        } else {
            // English content
            $('#siteTitle').text('Autistic Mindset');
            $('#SiteTheem').text('Autism Is Not A Disability.');
            $('#aboutus').text('ABOUT US');
            $('#ABOUT').text('ABOUT');
            $('#TEAM').text('TEAM');
            $('#OURSERVICES').text('OUR SERVICES');
            $('#SpecialistCare').text('specialist care');
            $('#community').text('community');
            $('#contact').text('CONTACT');
            $('#LearnMore').text('Learn more');
            // ... Update other elements ...
        }
    }


    // Modal Image Gallery
    function onClick(element) {
        document.getElementById("img01").src = element.src;
        document.getElementById("modal01").style.display = "block";
        var captionText = document.getElementById("caption");
        captionText.innerHTML = element.alt;
}

    // Toggle between showing and hiding the sidebar when clicking the menu icon
    var mySidebar = document.getElementById("mySidebar");

    function w3_open() {
        mySidebar.style.display = mySidebar.style.display === 'block' ? 'none' : 'block';
    }

    // Close the sidebar with the close button
    function w3_close() {
        mySidebar.style.display = "none";
    }

