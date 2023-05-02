import logging as log

log.basicConfig(level=log.DEBUG,
                format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                datefmt='%I:%M:%S %p',
                handlers=[
                    log.FileHandler('capa_datos.log', encoding='utf-8'),
                    log.StreamHandler()
                ])


# if __name__ == '__main__':
#     log.debug("Level debug")
#     log.info("level info")
#     log.warning("level warning")
#     log.error("level error")
#     log.critical("level critical")
