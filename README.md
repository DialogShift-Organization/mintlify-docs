# DialogShift Support Documentation

This repository contains the support documentation for DialogShift, built using Mintlify.

## 📚 Documentation Guidelines

**For AI models and developers:** Please read the [MINTLIFY_GUIDELINES.md](./MINTLIFY_GUIDELINES.md) file for comprehensive instructions on how to work with this Mintlify documentation repository.

## 🚀 Quick Start

Click on `Use this template` to copy the Mintlify starter kit. The starter kit contains examples including

- Guide pages.
- Navigation
- Customizations
- API Reference pages
- Use of popular components

### Development

Install the [Mintlify CLI](https://www.npmjs.com/package/mint) to preview the documentation changes locally. To install, use the following command

```
npm i -g mint
```

Run the following command at the root of your documentation (where docs.json is)

```
mint dev
```

### Publishing Changes

Install our Github App to auto propagate changes from your repo to your deployment. Changes will be deployed to production automatically after pushing to the default branch. Find the link to install on your dashboard.

#### Troubleshooting

- It the dev environment isn't running - Run `mint install` it'll re-install dependencies.
- Page loads as a 404 - Make sure you are running in a folder with `docs.json`