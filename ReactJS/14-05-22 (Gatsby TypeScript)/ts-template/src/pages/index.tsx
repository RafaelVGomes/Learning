import * as React from "react"
import { Carousel } from 'react-responsive-carousel'
import { useStaticQuery, graphql } from 'gatsby'

import IndexHeader from "../components/index/header/header.layout"
import IndexFooter from "../components/index/footer/footer.layout"
import * as style from "../components/index/index.module.sass"

const IndexPage = (): JSX.Element => {
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
    <main>
      <header>
        <IndexHeader></IndexHeader>
      </header>
      
      <body className={style.container}>
        <div className={style.siteTitle}>
          {data.site.siteMetadata.title}
        </div>
        
        <h1 className={style.pageTitle}>Home Page</h1>
        <p>Body Test</p>
      </body>

      <footer className={style.footer}>
        <IndexFooter></IndexFooter>
      </footer>
    </main>
  )
}

export default IndexPage
