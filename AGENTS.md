# Mintlify Documentation Guidelines for AI Models

## Overview
This repository uses Mintlify, a modern documentation platform that uses MDX (Markdown + JSX) for content creation. This guide helps AI models understand how to properly create and maintain documentation in this system.

## What is Mintlify?
Mintlify is a documentation platform that:
- Uses MDX files for content (`.mdx` extension)
- Supports React/JSX components within Markdown
- Has a specific configuration structure (`docs.json`)
- Provides built-in components for enhanced documentation
- Supports dark/light mode, syntax highlighting, and API documentation

## File Structure

### Key Files
- `docs.json` - Main configuration file that controls navigation, theme, and settings
- `*.mdx` files - Content files using MDX format
- `/images/` - Store images here
- `/logo/` - Logo files for light/dark modes
- `/snippets/` - Reusable content snippets
- `/de` - Path for german articles
- `/en` - Path for english articles

## MDX File Format

### Required Frontmatter
Every MDX file MUST start with frontmatter:
```mdx
---
title: "Page Title"
description: "Brief description of the page"
---
```
Important: title and description will be shown on the page to the user. So no need to duplicate it again in the section below.

### Optional Frontmatter Fields
```mdx
---
title: "Page Title"
description: "Description"
icon: "icon-name"  # FontAwesome icon
sidebarTitle: "Shorter Title"  # If different from title
"og:title": "Open Graph Title"
"og:description": "Open Graph Description"
---
```

### Important: No Duplicate Titles or Descriptions
**DO NOT** add content that duplicates the frontmatter title or description. Mintlify automatically displays both the frontmatter title and description.

❌ **WRONG** - Creates duplicate titles and descriptions:
```mdx
---
title: "WhatsApp Setup Guide"
description: "How to configure WhatsApp for your hotel"
---

# WhatsApp Setup Guide  <!-- Duplicates title -->
Learn how to configure WhatsApp for your hotel.  <!-- Duplicates description -->
```

✅ **CORRECT** - Let frontmatter handle title and description:
```mdx
---
title: "WhatsApp Setup Guide"
description: "How to configure WhatsApp for your hotel"
---

## Step 1: Initial Setup
Start directly with content sections...
```

## Available Mintlify Components

### 1. Note/Warning/Info Blocks
```mdx
<Note>
  This is a note with helpful information.
</Note>

<Warning>
  This is a warning message.
</Warning>

<Info>
  This is an info block.
</Info>

<Tip>
  This is a helpful tip.
</Tip>
```

### 2. Card Components
```mdx
<Card
  title="Card Title"
  icon="icon-name"
  href="/path/to/page"
>
  Card description text
</Card>

<CardGroup cols={2}>
  <Card title="Card 1" icon="icon1" href="/page1">
    Description 1
  </Card>
  <Card title="Card 2" icon="icon2" href="/page2">
    Description 2
  </Card>
</CardGroup>
```

### 3. Steps Component
```mdx
<Steps>
  <Step title="First Step">
    Description of the first step
  </Step>
  <Step title="Second Step">
    Description of the second step
  </Step>
</Steps>
```

### 4. Code Blocks
```mdx
```javascript
// Use triple backticks with language identifier
const example = "code";
```

```json filename="example.json"
{
  "key": "value"
}
```
```

### 5. Tabs Component
```mdx
<Tabs>
  <Tab title="Tab 1">
    Content for tab 1
  </Tab>
  <Tab title="Tab 2">
    Content for tab 2
  </Tab>
</Tabs>
```

### 6. Accordions
```mdx
<AccordionGroup>
  <Accordion title="First Question">
    Answer to the first question
  </Accordion>
  <Accordion title="Second Question">
    Answer to the second question
  </Accordion>
</AccordionGroup>
```

### 7. Frame Component (for images/videos)
```mdx
<Frame>
  <img src="/images/example.png" alt="Description" />
</Frame>
```

## Adding Pages to Navigation

### Understanding docs.json Structure
The navigation is defined in `docs.json`:
```json
{
  "navigation": {
    "tabs": [
      {
        "tab": "Tab Name",
        "groups": [
          {
            "group": "Group Name",
            "pages": [
              "path/to/page1",
              "path/to/page2"
            ]
          }
        ]
      }
    ]
  }
}
```

### Rules for Navigation
1. Page paths in `docs.json` are relative to the root and WITHOUT the `.mdx` extension
2. The order in the `pages` array determines the sidebar order
3. Groups can be nested within tabs
4. Use forward slashes for paths (e.g., `"de/user-erstellen"`)

## Best Practices

### 1. File Naming
- Use kebab-case for file names: `user-guide.mdx`, not `userGuide.mdx`
- Be descriptive but concise
- For localized content, use folders: `/de/`, `/en/`, etc.

### 2. Images
- Store in `/images/` directory
- Use descriptive names
- Always include alt text
- For theme-specific images:
```mdx
<img
  className="block dark:hidden"
  src="/images/hero-light.png"
  alt="Hero Light"
/>
<img
  className="hidden dark:block"
  src="/images/hero-dark.png"
  alt="Hero Dark"
/>
```

### 3. Links
- Internal links: Use relative paths without `.mdx`: `[Link Text](/path/to/page)`
- External links: `[Link Text](https://example.com)`
- Email links: `[Email](mailto:email@example.com)`

### 4. Styling
- Use `className` instead of `class` (React convention)
- Tailwind CSS classes are available
- Dark mode is handled automatically with `dark:` prefix

### 5. API Documentation
- OpenAPI specs go in `/api-reference/openapi.json`
- Mintlify automatically generates API documentation from OpenAPI specs

## Common Tasks

### Adding a New Page
1. Create the `.mdx` file with proper frontmatter
2. Add the page path to `docs.json` in the appropriate group
3. Ensure the path in `docs.json` matches the file location (without `.mdx`)

### Creating a New Section
1. Create a new folder for organization
2. Add MDX files to the folder
3. Update `docs.json` to include a new group or tab

### Adding Interactive Elements
- Use Mintlify components for interactivity
- Avoid custom JavaScript unless necessary
- Leverage built-in components before creating custom ones

## Example: Creating a Support Page

1. Create file: `support/faq.mdx`
```mdx
---
title: "Frequently Asked Questions"
description: "Common questions and answers about our product"
---


2. Update `docs.json`:
```json
{
  "group": "Support",
  "pages": [
    "support/faq"
  ]
}
```

## Debugging Tips
1. Check frontmatter syntax - YAML errors are common
2. Ensure component names are capitalized
3. Verify file paths in `docs.json` match actual file locations
4. Use the Mintlify development server to preview changes
5. Check for unclosed JSX tags

## Resources
- [Mintlify Documentation](https://mintlify.com/docs)
- [MDX Documentation](https://mdxjs.com/)
- Component examples are in `/essentials/` folder of this repo

Remember: When in doubt, check existing files in this repository for examples of proper syntax and structure.

