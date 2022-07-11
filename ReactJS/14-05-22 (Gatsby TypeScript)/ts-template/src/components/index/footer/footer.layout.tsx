import * as React from "react"
import { Link } from "gatsby"
import * as style from "./footer.module.sass"

const IndexFooter = (): JSX.Element => {
  return(
    <nav>
      <p>Footer test</p>
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

export default IndexFooter