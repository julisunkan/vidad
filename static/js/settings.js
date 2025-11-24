// Load saved settings on page load
document.addEventListener('DOMContentLoaded', function() {
    loadSettings();
});

// Color picker synchronization
const bgColor = document.getElementById('bgColor');
const bgColorHex = document.getElementById('bgColorHex');
const colorPreview = document.getElementById('colorPreview');

bgColor.addEventListener('input', function() {
        const color = this.value;
        document.getElementById('bgColorHex').value = color;
        const preview = document.getElementById('colorPreview');
        preview.style.backgroundColor = color;
        preview.style.transform = 'scale(1.05)';
        setTimeout(() => {
            preview.style.transform = 'scale(1)';
        }, 200);
    });

    document.getElementById('bgColorHex').addEventListener('input', function() {
        const color = this.value;
        if (/^#[0-9A-F]{6}$/i.test(color)) {
            document.getElementById('bgColor').value = color;
            const preview = document.getElementById('colorPreview');
            preview.style.backgroundColor = color;
            preview.style.transform = 'scale(1.05)';
            setTimeout(() => {
                preview.style.transform = 'scale(1)';
            }, 200);
        }
    });


// Save settings
document.getElementById('settingsForm').addEventListener('submit', function(e) {
    e.preventDefault();

    const settings = {
        background_color: document.getElementById('bgColor').value
    };

    // Save only non-sensitive settings to localStorage
    localStorage.setItem('videoGenSettings', JSON.stringify(settings));

    // Show success message
    const successMessage = document.getElementById('successMessage');
    const errorMessage = document.getElementById('errorMessage');

    successMessage.classList.remove('d-none');
    errorMessage.classList.add('d-none');

    // Hide success message after 3 seconds
    setTimeout(() => {
        successMessage.classList.add('d-none');
    }, 3000);
});

// Load settings from localStorage
function loadSettings() {
    const savedSettings = localStorage.getItem('videoGenSettings');

    if (savedSettings) {
        try {
            const settings = JSON.parse(savedSettings);
            if (settings.background_color) {
                document.getElementById('bgColor').value = settings.background_color;
                document.getElementById('bgColorHex').value = settings.background_color;
                document.getElementById('colorPreview').style.backgroundColor = settings.background_color;
            }
        } catch (e) {
            console.error('Error loading settings:', e);
        }
    }
}