import streamlit as st
from tinydb import TinyDB, Query

db = TinyDB('data.json')
User = Query()
def update(name, price):
    db.update({'price': price}, User.name == 'name')

st.markdown('<style>.block-container {direction : rtl}</style>', unsafe_allow_html=True)
st.title('فروشگاه جواهرات ص')
Menu = ['دستبند','گردنبند','ورود اعضا']
choise = st.sidebar.selectbox('نوع محصول موردنظر خود را انتخاب کنید',Menu)
col1, col2 = st.columns(2)
if choise == 'دستبند':
    with col1:
        st.image('1.jpg')
    with col2:
        st.subheader('محصول شماره یک')
        result = db.get(User.name == '1')
        oncite = result['state']
        if oncite:
            ind = result['price']
            st.success(f'قیمت: {ind} تومان')
        else:
            st.error('ناموجود')
        st.warning('این محصول از طلای 18 عیار ساخته شده است.')
elif choise == 'گردنبند':
    with col1:
        st.image('2.jpg')
    with col2:  
        st.subheader('محصول شماره دو')
        result = db.get(User.name == '2')
        oncite = result['state']
        if oncite:
            ind = result['price']
            st.success(f'قیمت: {ind} تومان')
        else:
            st.error('ناموجود')
        st.warning('این محصول از طلای 18 عیار ساخته شده است.')

elif choise == 'ورود اعضا':
    st.table(db)
    option = st.selectbox(
    'نحوه بروزرسانی قیمت محصولات را مشخص کنید.',
    ('ورود دستی قیمت', 'بروزرسانی خودکار'))
    st.write('روش انتخابی شما:', option)
    if option == 'ورود دستی قیمت':
        name = st.text_input('نام محصول را وارد کنید')
        state = st.checkbox('آیا محصول موجود است؟')
        if state:
            price = st.text_input('قیمت محصول را وارد کنید')
        
        sell = st.button('done')
        # sell = st.checkbox('اعمال تغییرات؟')
        
        if name and sell:
            if state:
                db.update({'state': state}, User.name == name)
                db.update({'price': price}, User.name == name)
            else:
                db.update({'state': state}, User.name == name)
            st.success('saved')
    else:
        st.write('در دست ساخت!')
