
let deferredPrompt;

window.addEventListener('beforeinstallprompt', (e) => {
    e.preventDefault();
    deferredPrompt = e;
    
    const installBanner = document.createElement('div');
    installBanner.className = 'install-banner';
    installBanner.innerHTML = `
        <div class="install-content">
            <span>📱 Install Video Gen App</span>
            <button id="installBtn" class="btn btn-sm btn-primary">Install</button>
            <button id="dismissBtn" class="btn btn-sm btn-light">×</button>
        </div>
    `;
    document.body.appendChild(installBanner);
    
    document.getElementById('installBtn').addEventListener('click', async () => {
        deferredPrompt.prompt();
        const { outcome } = await deferredPrompt.userChoice;
        console.log(`User response: ${outcome}`);
        deferredPrompt = null;
        installBanner.remove();
    });
    
    document.getElementById('dismissBtn').addEventListener('click', () => {
        installBanner.remove();
    });
});

window.addEventListener('appinstalled', () => {
    console.log('PWA installed successfully');
});
