let currentTemplate = null;

document.getElementById('templateSelect').addEventListener('change', function() {
    const templateId = this.value;
    
    if (!templateId) {
        document.getElementById('templateInfo').classList.add('d-none');
        document.getElementById('imageInputs').innerHTML = '';
        return;
    }
    
    fetch(`/get_template/${templateId}`)
        .then(response => response.json())
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
    
    if (!currentTemplate) {
        alert('Please select a video template');
        return;
    }
    
    const formData = new FormData(this);
    
    document.getElementById('generateBtn').disabled = true;
    document.getElementById('btnText').classList.add('d-none');
    document.getElementById('btnSpinner').classList.remove('d-none');
    document.getElementById('progressSection').classList.remove('d-none');
    document.getElementById('resultSection').classList.add('d-none');
    document.getElementById('errorSection').classList.add('d-none');
    
    fetch('/generate_video', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
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
