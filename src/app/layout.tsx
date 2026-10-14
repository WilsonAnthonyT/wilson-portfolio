import type {Metadata,Viewport} from 'next';
import './globals.css';
export const metadata:Metadata={title:{default:'Wilson Antony Thang — Software & AI Engineer',template:'%s | Wilson Antony Thang'},description:'Wilson Antony Thang — NTHU EECS undergraduate building AI applications, mobile products, and systems software. Selected projects, case studies and résumé.',openGraph:{type:'website',title:'Wilson Antony Thang — AI · Mobile · Systems',description:'Engineering thoughtful software, from agentic AI to embedded systems.',images:[{url:'/og.png',width:1200,height:630,alt:'Wilson Antony Thang — AI Engineering, Mobile, Systems'}]},robots:{index:true,follow:true}};
export const viewport:Viewport={width:'device-width',initialScale:1,themeColor:'#090f1f'};
export default function RootLayout({children}:{children:React.ReactNode}){return <html lang="en" suppressHydrationWarning><body><a className="skip-link" href="#main">Skip to main content</a>{children}</body></html>}
