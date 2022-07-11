module.exports = {
  siteMetadata: {
    title: `Gatsby Tutorial`,
    siteUrl: `https://www.yourdomain.tld`,
  },
  plugins: [
    `gatsby-plugin-pnpm`,
    `gatsby-plugin-image`,
    `gatsby-plugin-sharp`,
		`gatsby-transformer-sharp`,
		`gatsby-plugin-mdx`,
    {
      resolve: "gatsby-source-filesystem",
      options: {
        name: `blog`,
        path: `${__dirname}/blog`
      }
    }
  ],
}
