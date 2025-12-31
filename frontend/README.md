# Exit Three - Marketing Website

**Modern B2B SaaS marketing website** built with Nuxt 3, Vue 3, TypeScript, and Tailwind CSS. Features comprehensive SEO optimization, multi-language support (EN/HR), and performance-first architecture.

## 📋 Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Development](#development)
- [Production Deployment](#production-deployment)
- [Environment Variables](#environment-variables)
- [API Endpoints](#api-endpoints)
- [Security](#security)
- [Performance](#performance)

## ✨ Features

- **Modern Stack**: Nuxt 3 + Vue 3 + TypeScript + Tailwind CSS
- **SEO Optimized**: Sitemap generation, robots.txt, meta tags, Open Graph
- **Multi-language**: English and Croatian (i18n)
- **Performance**: Lazy hydration, code splitting, image optimization
- **Analytics**: Google Tag Manager integration with GDPR compliance
- **Security**: CSP headers, XSS protection, input validation
- **Accessibility**: ARIA labels, keyboard navigation, semantic HTML

## 📦 Prerequisites

- Node.js 18+ or 20+ (LTS recommended)
- npm 9+ or pnpm 8+
- Git

## 🚀 Setup

### 1. Clone the repository

```bash
git clone <repository-url>
cd exithree
```

### 2. Install dependencies

```bash
npm install
```

### 3. Configure environment variables

Copy the example environment file and fill in your values:

```bash
cp .env.example .env
```

**Required environment variables:**
- `NUXT_PUBLIC_BASE_URL` - Your domain URL
- `BASIC_API_KEY` - Backend API authentication key (server-side only)
- `NUXT_PUBLIC_GTAG_ID` - Google Tag Manager ID (optional for development)

See [Environment Variables](#environment-variables) section for full details.

## 💻 Development

Start the development server on `http://localhost:3000`:

```bash
npm run dev
```

### Code Quality

```bash
# Run ESLint + Prettier check
npm run lint

# Auto-fix linting issues and format code
npm run lintfix
```

## 🏗️ Production Deployment

### Build for Production

```bash
# Generate static site
npm run build

# Preview production build locally
npm run preview
```

### Pre-deployment Checklist

- [ ] All environment variables configured in `.env`
- [ ] Security headers configured in `nuxt.config.ts`
- [ ] API keys moved to private runtime config
- [ ] Analytics configured (Google Tag Manager)
- [ ] SSL certificate installed
- [ ] Test health check endpoint: `GET /api/health`

### Deployment Options

**Option 1: Vercel (Recommended)**
- Zero-config deployment
- Configure environment variables in Vercel dashboard

**Option 2: Netlify**
- Similar to Vercel with built-in form spam protection

**Option 3: Docker**
- See `Dockerfile` in project root
- Run: `docker-compose up -d`

**Option 4: VPS**
- Use PM2 for process management
- Configure reverse proxy (nginx/caddy)

## 🔐 Environment Variables

### Required Variables

| Variable | Type | Description |
|----------|------|-------------|
| `NUXT_PUBLIC_BASE_URL` | Public | Your domain URL |
| `BASIC_API_KEY` | Private | Backend API authentication key |

### Optional Variables

| Variable | Type | Description |
|----------|------|-------------|
| `NUXT_PUBLIC_GTAG_ID` | Public | Google Tag Manager container ID |
| `MAIL_SMTP_HOST` | Private | SMTP server for email |
| `MAIL_SMTP_PORT` | Private | SMTP port |
| `MAIL_USER` | Private | SMTP username |
| `MAIL_PASS` | Private | SMTP password |

**⚠️ Important:** Variables prefixed with `NUXT_PUBLIC_` are exposed to the browser. Private variables (without prefix) are server-side only.

## 🔌 API Endpoints

- `GET /api/health` - Health check endpoint
- `POST /api/submit-lead` - Submit contact form (proxies to backend)
- `POST /api/send-email` - Send email via Nodemailer (optional)

## 🔒 Security

### Implemented Features

✅ Security Headers (CSP, X-Frame-Options, HSTS, etc.)
✅ API keys stored server-side only
✅ Input validation and sanitization
✅ GDPR-compliant cookie consent
✅ Environment variable validation

## ⚡ Performance

- **Lazy Hydration**: Delayed hydration for faster TTI
- **Code Splitting**: Automatic vendor chunking
- **Image Optimization**: WebP/AVIF formats with lazy loading
- **CSS Optimization**: Tailwind CSS purging

### Performance Monitoring

```bash
# Generate Lighthouse report
npx lighthouse http://localhost:3000 --view

# Analyze bundle size
npx nuxi analyze
```

## 📚 Additional Documentation

For a comprehensive production readiness review and improvement suggestions, see `claude.md` in the project root.

## 📄 License

Proprietary - Exit Three

---

**Built with ❤️ by Exit Three**
