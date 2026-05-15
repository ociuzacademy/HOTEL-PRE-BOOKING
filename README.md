## Google Maps API Configuration

This project integrates the Google Maps JavaScript API to provide map-based functionality across multiple modules. For security and best practices, the API key has been excluded from the source code repository.

### Setup Instructions

1. Generate a Google Maps API Key
   Create or select a project in the [Google Cloud Console](https://console.cloud.google.com/?utm_source=chatgpt.com) and generate a new API key.

2. Enable Required API Services
   Ensure that the following service is enabled for your Google Cloud project:

   * Maps JavaScript API

3. Update the API Key in Project Templates
   Search the project for the placeholder:

   ```text
   INSERT_YOUR_API_KEY_HERE
   ```

   Replace it with your generated API key in the following files:

   * `templates/index.html`
   * `templates/admin/admin_home.html`
   * `templates/worker/worker_home.html`
   * `templates/restaurant/restaurant_home.html`

### Security Recommendation

For production deployments, it is strongly recommended to restrict your API key within the Google Cloud Console by:

* Limiting usage to your application's domain or IP address
* Restricting access to only the required Google Maps APIs

This helps prevent unauthorized usage and unexpected billing charges.
