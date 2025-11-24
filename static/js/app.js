let currentTemplate = null;
let generationMode = 'template';

// Mode switching
document.querySelectorAll('input[name="generationMode"]').forEach(radio => {
    radio.addEventListener('change', function() {
        generationMode = this.value;
        const templateFields = document.getElementById('templateFields');
        const soraFields = document.getElementById('soraFields');
        const modeDescription = document.getElementById('modeDescription');
        const templateSelect = document.getElementById('templateSelect');
        
        if (generationMode === 'sora') {
            templateFields.style.display = 'none';
            soraFields.style.display = 'block';
            modeDescription.textContent = 'Use OpenAI Sora AI to generate videos from text descriptions';
            templateSelect.removeAttribute('required');
        } else {
            templateFields.style.display = 'block';
            soraFields.style.display = 'none';
            modeDescription.textContent = 'Use pre-built templates with images and text overlays';
            templateSelect.setAttribute('required', 'required');
        }
    });
});

// Sora duration slider
const soraDuration = document.getElementById('soraDuration');
const durationValue = document.getElementById('durationValue');
if (soraDuration && durationValue) {
    soraDuration.addEventListener('input', function() {
        durationValue.textContent = this.value;
    });
}

// API provider selector
const apiProvider = document.getElementById('apiProvider');
const providerInfo = document.getElementById('providerInfo');
if (apiProvider && providerInfo) {
    apiProvider.addEventListener('change', function() {
        if (this.value === 'sora') {
            providerInfo.innerHTML = '<strong>⚠️ OpenAI Sora:</strong> Requires paid OpenAI API key with Sora access. Add OPENAI_API_KEY to Secrets. Cost: ~$0.10-$0.50 per second.';
            providerInfo.className = 'alert alert-warning';
        } else {
            providerInfo.innerHTML = '<strong>💡 Replicate (Free tier available):</strong> Get API key at replicate.com. Free $5 credits to start. Cost: ~$0.006 per second of video.';
            providerInfo.className = 'alert alert-info';
        }
    });
}

document.getElementById('templateSelect').addEventListener('change', function() {
    const templateId = this.value;
    
    if (!templateId) {
        document.getElementById('templateInfo').classList.add('d-none');
        document.getElementById('imageInputs').innerHTML = '';
        return;
    }
    
    fetch(`/get_template/${templateId}`)
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return response.json();
        })
        .then(template => {
            currentTemplate = template;
            
            document.getElementById('templateDescription').textContent = template.description;
            document.getElementById('templateDuration').textContent = template.duration;
            document.getElementById('templateSlots').textContent = template.image_slots;
            document.getElementById('templateInfo').classList.remove('d-none');
            
            const imageInputsContainer = document.getElementById('imageInputs');
            imageInputsContainer.innerHTML = '';
            
            for (let i = 0; i < template.image_slots; i++) {
                const inputGroup = document.createElement('div');
                inputGroup.className = 'mb-2';
                inputGroup.innerHTML = `
                    <label for="image_${i}" class="form-label">Image ${i + 1}</label>
                    <input type="file" class="form-control" id="image_${i}" name="image_${i}" 
                           accept=".png,.jpg,.jpeg,.gif,.webp">
                `;
                imageInputsContainer.appendChild(inputGroup);
            }
        })
        .catch(error => {
            console.error('Error fetching template:', error);
        });
});

document.getElementById('videoForm').addEventListener('submit', function(e) {
    e.preventDefault();
    
    if (generationMode === 'template' && !currentTemplate) {
        alert('Please select a video template');
        return;
    }
    
    if (generationMode === 'sora') {
        const prompt = document.getElementById('soraPrompt').value.trim();
        if (!prompt) {
            alert('Please enter a video description');
            return;
        }
    }
    
    // Load settings from localStorage (background color only)
    const savedSettings = localStorage.getItem('videoGenSettings');
    let settings = {};
    if (savedSettings) {
        try {
            settings = JSON.parse(savedSettings);
        } catch (e) {
            console.error('Error loading settings:', e);
        }
    }
    
    const formData = new FormData(this);
    
    // Add background color from settings if available
    if (settings.background_color && generationMode === 'template') {
        formData.append('background_color', settings.background_color);
    }
    
    let endpoint = '/generate_video';
    let requestBody = formData;
    
    // Handle Sora generation
    if (generationMode === 'sora') {
        endpoint = '/generate_sora_video';
        const apiProvider = document.getElementById('apiProvider').value;
        const soraData = {
            prompt: document.getElementById('soraPrompt').value,
            duration: parseInt(document.getElementById('soraDuration').value),
            size: document.getElementById('soraSize').value,
            use_image: false,
            api_provider: apiProvider
        };
        requestBody = JSON.stringify(soraData);
    }
    
    document.getElementById('generateBtn').disabled = true;
    document.getElementById('btnText').classList.add('d-none');
    document.getElementById('btnSpinner').classList.remove('d-none');
    document.getElementById('progressSection').classList.remove('d-none');
    document.getElementById('resultSection').classList.add('d-none');
    const errorSection = document.getElementById('errorSection');
    if (errorSection) errorSection.classList.add('d-none');
    
    const fetchOptions = {
        method: 'POST',
        body: requestBody
    };
    
    if (generationMode === 'sora') {
        fetchOptions.headers = {
            'Content-Type': 'application/json'
        };
    }
    
    fetch(endpoint, fetchOptions)
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
    })
    .then(data => {
        document.getElementById('generateBtn').disabled = false;
        document.getElementById('btnText').classList.remove('d-none');
        document.getElementById('btnSpinner').classList.add('d-none');
        document.getElementById('progressSection').classList.add('d-none');
        
        if (data.success) {
            const videoPreview = document.getElementById('videoPreview');
            const downloadLink = document.getElementById('downloadLink');
            
            videoPreview.src = data.video_url.replace('/download_video/', '/preview_video/');
            downloadLink.href = data.video_url;
            
            document.getElementById('resultSection').classList.remove('d-none');
            
            document.getElementById('resultSection').scrollIntoView({ behavior: 'smooth' });
        } else {
            document.getElementById('errorMessage').textContent = data.error || 'Unknown error occurred';
            document.getElementById('errorSection').classList.remove('d-none');
        }
    })
    .catch(error => {
        document.getElementById('generateBtn').disabled = false;
        document.getElementById('btnText').classList.remove('d-none');
        document.getElementById('btnSpinner').classList.add('d-none');
        document.getElementById('progressSection').classList.add('d-none');
        
        document.getElementById('errorMessage').textContent = error.message || 'Failed to generate video';
        document.getElementById('errorSection').classList.remove('d-none');
    });
});
