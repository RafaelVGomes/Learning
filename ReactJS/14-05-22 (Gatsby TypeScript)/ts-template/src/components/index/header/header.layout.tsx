import * as React from "react"
import { Link } from "gatsby"
import * as style from "./header.module.sass"

const IndexHeader = (): JSX.Element => {
  return(
    <nav>
      <p>Header test</p>
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
  )
}

export default IndexHeader