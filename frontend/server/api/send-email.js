import nodemailer from 'nodemailer'

// Input sanitization helper - removes potentially dangerous characters
function sanitizeInput(input, maxLength = 255) {
  if (!input || typeof input !== 'string') return ''

  // Trim and limit length
  let sanitized = input.trim().substring(0, maxLength)

  // Remove any control characters and non-printable characters
  sanitized = sanitized.replace(/[\x00-\x1F\x7F-\x9F]/g, '')

  // Remove HTML tags (basic protection)
  sanitized = sanitized.replace(/<[^>]*>/g, '')

  return sanitized
}

// Email validation helper
function isValidEmail(email) {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
  return emailRegex.test(email) && email.length <= 254
}

export default defineEventHandler(async (event) => {
  try {
    const config = useRuntimeConfig()
    const body = await readBody(event)

    // Validate required fields
    if (!body || typeof body !== 'object') {
      throw createError({
        statusCode: 400,
        message: 'Invalid request body'
      })
    }

    // Validate and sanitize inputs
    const name = sanitizeInput(body.name, 100)
    const jobTitle = sanitizeInput(body.jobTitle, 100)
    const company = sanitizeInput(body.company, 100)
    const email = sanitizeInput(body.email, 254)
    const topic = sanitizeInput(body.topic, 200)

    // Validate required fields
    if (!name || !email || !topic) {
      throw createError({
        statusCode: 400,
        message: 'Missing required fields: name, email, and topic are required'
      })
    }

    // Validate email format
    if (!isValidEmail(email)) {
      throw createError({
        statusCode: 400,
        message: 'Invalid email address format'
      })
    }

    const transporter = nodemailer.createTransport({
      host: config.MAIL_SMTP_HOST,
      port: Number(config.MAIL_SMTP_PORT),
      secure: true,
      auth: {
        user: config.MAIL_USER,
        pass: config.MAIL_PASS,
      },
    })

    const mailOptions = {
      from: config.MAIL_USER,
      to: config.MAIL_USER,
      subject: `Lead - ${topic}`,
      text: `
        Name: ${name}
        Job Title: ${jobTitle || 'Not provided'}
        Company: ${company || 'Not provided'}
        Email: ${email}
        Topic: ${topic}
      `,
    }

    await transporter.sendMail(mailOptions)

    return { success: true, message: "Email sent successfully!" }
  } catch (error) {
    console.error("Email sending error:", error)

    // Return appropriate error response
    if (error.statusCode) {
      throw error
    }

    throw createError({
      statusCode: 500,
      message: "Failed to send email."
    })
  }
})
