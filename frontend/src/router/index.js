import { createRouter, createWebHistory } from 'vue-router'
import { useUserStore } from '@/stores/user'
import HomeView from '@/views/HomeView.vue'
import ArticlesView from '@/views/ArticlesView.vue'
import CategoryView from '@/views/CategoryView.vue'
import IDArticleView from '@/views/IDArticleView.vue'
import CreateArticleView from '@/views/CreateArticleView.vue'
import NotFoundView from '@/views/NotFoundView.vue'
import { ElMessage } from 'element-plus'

// 路由守卫
const isAdmin = (to, from, next) => {
  const userStore = useUserStore()
  if (userStore.Role === 'admin') {
    next() // 用户是管理员，允许访问
  } else {
    ElMessage.warning('您没有权限访问此页面') // 显示警告消息
    userStore.LoginVisibility = true // 显示登录框
    next({ name: 'home' }) // 用户不是管理员，重定向到首页或其他页面
  }
}

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
        { path: 'articles/:id', name: 'id-article', component: IDArticleView },
        { path: 'categories', name: 'categories', component: CategoryView },
        {
          path: 'categories/:tag',
          name: 'tag-category',
          component: CategoryView
        },
        {
          path: 'create',
          name: 'create-article',
          component: CreateArticleView,
          beforeEnter: isAdmin // 添加路由守卫
        }
      ]
    },
    {
      path: '/:catchAll(.*)', // 匹配所有未定义的路由
      name: 'not-found',
      component: NotFoundView
    }
  ]
})

export default router
