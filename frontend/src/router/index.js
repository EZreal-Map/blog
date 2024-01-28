import { createRouter, createWebHistory } from 'vue-router'

import HomeView from '@/views/HomeView.vue'
import ArticlesView from '@/views/ArticlesView.vue'
import CatogoryView from '@/views/CatogoryView.vue'
import IDArticleView from '@/views/IDArticleView.vue'
import CreateArticleView from '@/views/CreateArticleView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      redirect: '/blog/home'
    },
    {
      path: '/blog',
      redirect: '/blog/home',
      children: [
        { path: 'home', name: 'home', component: HomeView },
        { path: 'articles', name: 'articles', component: ArticlesView },
        { path: 'catogory', name: 'catogory', component: CatogoryView },
        { path: 'article/:id', name: 'id-article', component: IDArticleView },
        { path: 'create', name: 'create-article', component: CreateArticleView }
      ]
    }
  ]
})

export default router
