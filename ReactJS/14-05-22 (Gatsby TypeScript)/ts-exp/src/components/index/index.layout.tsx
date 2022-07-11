import * as React from 'react'
import { Helmet } from "react-helmet"
import { Link, useStaticQuery, graphql } from 'gatsby'
import * as style from './layout.module.sass'

type params = {
  pageTitle: string,
  children?: any
}

const IndexLayout = ({ pageTitle, children }: params): JSX.Element => {
  const data = useStaticQuery(graphql`
    query {
      site {
        siteMetadata {
          title
        }
      }
    }  
  `)
  
  return (
    <div className={style.container}>
      <Helmet>
        <meta charSet="utf-8" />
        <title>{pageTitle} | {data.site.siteMetadata.title}</title>
      </Helmet>
      
      <main>
        <header className={style.siteTitle}>
          {data.site.siteMetadata.title}
          <nav>
            <ul className={style.navLinks}>
              <li className={style.navLinkItem}>
                <Link to="/" className={style.navLinkText}>Home</Link>
              </li>
              <li className={style.navLinkItem}>
                <Link to="/about" className={style.navLinkText}>About</Link>
              </li>
              <li className={style.navLinkItem}>
                <Link to="/blog" className={style.navLinkText}>Blog</Link>
              </li>
            </ul>
          </nav>
        </header>

        <body>
          <h1 className={style.heading}>{pageTitle}</h1>
          {children}
        </body>

        <footer>

        </footer>
      </main>
    </div>
  )
}

export default IndexLayout