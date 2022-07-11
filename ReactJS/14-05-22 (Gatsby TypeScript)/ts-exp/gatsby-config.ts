import type { GatsbyConfig } from "gatsby"
import path from "path"

const config: GatsbyConfig = {
  siteMetadata: {
    title: `*.{ts, tsx} Experience on Gatsby`,
  },
  plugins: [
    `gatsby-plugin-pnpm`,
    `gatsby-plugin-sass`,
    // {
    //   resolve: `gatsby-source-filesystem`,
    //   options: {
    //     path: path.resolve(`./src/components/**/*.html`)
    //   }
    // }
  ],
}

export default config
