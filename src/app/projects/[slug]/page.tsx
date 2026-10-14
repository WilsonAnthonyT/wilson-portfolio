import type {Metadata} from 'next';import {notFound} from 'next/navigation';import CaseStudy from '@/components/CaseStudy';import {projects,getProject} from '@/content/projects';
export function generateStaticParams(){return projects.map(p=>({slug:p.slug}));}
export async function generateMetadata({params}:{params:Promise<{slug:string}>}):Promise<Metadata>{const {slug}=await params;const p=getProject(slug);return {title:p?.title??'Project',description:p?.summary};}
export default async function Page({params}:{params:Promise<{slug:string}>}){const {slug}=await params;const project=getProject(slug);if(!project)notFound();return <CaseStudy project={project}/>}
