export default defineEventHandler(async (event) => {
  try {
    const config = useRuntimeConfig()
    const body = await readBody(event)

    // Validate required fields
    if (!body.full_name || !body.position || !body.company_name || !body.email || !body.category) {
      throw createError({
        statusCode: 400,
        statusMessage: 'Missing required fields'
      })
    }

    // Validate email format
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
    if (!emailRegex.test(body.email)) {
      throw createError({
        statusCode: 400,
        statusMessage: 'Invalid email format'
      })
    }

    // Validate category
    const validCategories = [
      'web_dev',
      'mobile_dev',
      'automated_testing',
      'social_media_auto',
      'ecommerce_auto',
      'sales_auto'
    ]
    if (!validCategories.includes(body.category)) {
      throw createError({
        statusCode: 400,
        statusMessage: 'Invalid category'
      })
    }

    // Sanitize input (trim and limit length)
    const sanitizedData = {
      full_name: body.full_name.trim().substring(0, 100),
      position: body.position.trim().substring(0, 100),
      company_name: body.company_name.trim().substring(0, 100),
      email: body.email.trim().substring(0, 100),
      category: body.category
    }

    // Forward to backend API with private API key
    const response = await $fetch(`${config.public.baseUrl}/backend/api/leads/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Basic ${config.basicApiKey}`
      },
      body: sanitizedData
    })

    return {
      success: true,
      message: 'Lead submitted successfully'
    }
  } catch (error: any) {
    console.error('Lead submission error:', error)

    // Return appropriate error response
    if (error.statusCode) {
      throw error
    }

    throw createError({
      statusCode: 500,
      statusMessage: 'Failed to submit lead'
    })
  }
})
