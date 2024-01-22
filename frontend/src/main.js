import { createApp } from 'vue'
import pinia from '@/stores/index'
import App from './App.vue'
import router from './router'

const app = createApp(App)

app.use(pinia) // pinia持久化后的封装
app.use(router)
app.mount('#app')
