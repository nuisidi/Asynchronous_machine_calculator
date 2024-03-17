import flet as ft
from basics import ElectricSystem


def main(page):

    def return_to_main_menu(e):
        page.clean()
        main(page)

    def dialog_dismissed(e):
        page.clean()
        main(page)

    cupertino_alert_dialog = ft.CupertinoAlertDialog(
        title=ft.Text("Ошибка!"),
        content=ft.Text(""),
        on_dismiss=dialog_dismissed,
        actions=[ft.CupertinoDialogAction("Вернуться",
                 is_default_action=True,
                 on_click=return_to_main_menu)]
    )

    def open_cupertino_dialog(e):
        page.dialog = cupertino_alert_dialog
        cupertino_alert_dialog.open = True
        page.update()

    def btn_click(e):
        try:
            page.clean()
            page.scroll = "always"
            page.title = "Результаты"
            p = float(p_kw.value)
            un = float(un_v.value)
            w1 = float(w1_val.value)
            w2 = float(w2_val.value)
            k01 = float(k01_val.value)
            k02 = float(k02_val.value)
            r1 = float(r1_om.value)
            r2 = float(r2_om.value)
            x1 = float(x1_om.value)
            x2 = float(x2_om.value)
            m1 = float(m1_val.value)
            m2 = float(m2_val.value)
            poles = float(poles_val.value)
            f1 = float(f1_hz.value)
            ns = float(ns_val.value)
            sn = float(sn_perc.value)
            electric_system = ElectricSystem(p, un, w1, w2, k01,
                                             k02, r1, r2, x1, x2,
                                             m1, m2, poles, f1, ns, sn)
            result = electric_system.calculate()
            for key, value in result.items():
                page.add(ft.Text(f"{key}: {value}", theme_style=ft.Theme.text_theme))

            page.add(ft.ElevatedButton('Начать расчет заново', on_click=return_to_main_menu))
        except Exception as ex:
            open_cupertino_dialog(e)

    page.title = "Данные Асинхронного двигателя"
    p_kw = ft.TextField(label="Полная мощность P, кВт", autofocus=True)
    un_v = ft.TextField(label="Фазное напряжение Un, В")
    w1_val = ft.TextField(label="Количество обмоток статора")
    w2_val = ft.TextField(label="Количество обмоток ротора")
    k01_val = ft.TextField(label="Обмоточный коэффициент статора")
    k02_val = ft.TextField(label="Обмоточный коэффициент ротора")
    r1_om = ft.TextField(label="Активное сопротивление обмоток ротора, Ом")
    r2_om = ft.TextField(label="Активное сопротивление обмоток статора, Ом")
    x1_om = ft.TextField(label="Индуктивное сопротивление обмоток статора, Ом")
    x2_om = ft.TextField(label="Индуктивное сопротивление обмоток ротора, Ом")
    m1_val = ft.TextField(label="Число фаз обмоток статора")
    m2_val = ft.TextField(label="Число фаз обмоток ротора")
    poles_val = ft.TextField(label="Число пар полюсов")
    f1_hz = ft.TextField(label="Частота сети, Гц")
    ns_val = ft.TextField(label="Количество оборотов")
    sn_perc = ft.TextField(label="Номинальное скольжение, %")

    page.theme = ft.Theme(
        color_scheme=ft.ColorScheme(
            primary=ft.colors.PRIMARY,
            primary_container=ft.colors.ON_PRIMARY_CONTAINER
        )
    )

    page.scroll = "always"
    page.update()

    page.add(
        p_kw,
        un_v,
        w1_val,
        w2_val,
        k01_val,
        k02_val,
        r1_om,
        r2_om,
        x1_om,
        x2_om,
        m1_val,
        m2_val,
        poles_val,
        f1_hz,
        ns_val,
        sn_perc,
        ft.ElevatedButton("Расчитать!", on_click=btn_click)
    )


if __name__ == '__main__':
    ft.app(target=main)
