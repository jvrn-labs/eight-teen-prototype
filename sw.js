// Retired. v1 used to be installed at the site root with an offline cache.
// It now lives in /v1/ with its own worker, and the root link redirects to the
// current test build. Phones that still have the old root worker fetch this
// file, clear the old cache and unregister it. Keep this file for a few weeks.
self.addEventListener('install', () => self.skipWaiting());
self.addEventListener('activate', e => {
  e.waitUntil(
    caches.keys()
      .then(keys => Promise.all(keys.filter(k => k.startsWith('eightteen-') && !k.startsWith('eightteen-v1-')).map(k => caches.delete(k))))
      .then(() => self.registration.unregister())
      // Reload any open root page so it picks up the redirect now, not on the next visit.
      .then(() => self.clients.matchAll({ type: 'window' }))
      .then(clients => {
        const root = new URL(self.registration.scope).pathname;
        clients.forEach(c => {
          const path = new URL(c.url).pathname;
          if (path === root || path === root + 'index.html') c.navigate(c.url);
        });
      })
  );
});
