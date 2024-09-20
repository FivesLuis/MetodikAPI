USE [Metodik30]
GO
/****** Object:  StoredProcedure [dbo].[spActRuta]    Script Date: 20/09/2024 13:55:20 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

ALTER PROCEDURE [dbo].[spActRuta]
  @ID INT,
  @Ruta VARCHAR(50),
  @Zona VARCHAR(30),
  @Kms FLOAT,
  @Costo FLOAT,
  @SucursalID int,
  @DestinoID int,
  @OrigenID int,
  @Observaciones VARCHAR(100),
  @EstatusID INT,
  @Tiempo FLOAT,
  @Fecha date,
  @VehiculoID int, 
  @CostoInfantil int,
  @CostoAdulto int,
  @CostoInapan int
AS
BEGIN
    DECLARE
        @Ok INT,
        @Tipo VARCHAR(25), -- success, info, warning, error
        @Titulo VARCHAR(250),
        @Mensaje VARCHAR(250),
        @Posicion VARCHAR(25); -- toast + (Top Right, Bottom Right,  Bottom Left, Top Left, Top Full Width, Bottom Full Width, Top Center, Bottom Center)

    -- Check if necessary fields are provided
    IF ISNULL(@Ruta, '') = ''
    BEGIN
        SELECT 1 AS Ok, 'warning' AS Tipo, 'Ruta' AS Titulo, 'Ingresa un nombre para la Ruta' AS Mensaje, 'toast-top-right' AS Posicion;
        RETURN;
    END

    BEGIN TRY
        BEGIN TRANSACTION;

        -- Check if the record exists
        IF NOT EXISTS(SELECT 1 FROM ruta WHERE ID = @ID)
        BEGIN
            -- Insert new record
            INSERT INTO ruta (Ruta, Zona, Kms, Costo, SucursalID, DestinoID, OrigenID,  Observaciones, EstatusID, Tiempo, UltimoCambio, FechaRegistro, Fecha, VehiculoID, CostoInfantil, CostoAdulto, CostoInapan)
            VALUES (@Ruta, @Zona, @Kms, @Costo, @SucursalID, @DestinoID, @OrigenID, @Observaciones, @EstatusID, @Tiempo, GETDATE(), GETDATE(), @Fecha, @VehiculoID,@CostoInfantil, @CostoAdulto, @CostoInapan)

            COMMIT TRANSACTION;
            SELECT @Ok = 0, @Tipo = 'success', @Titulo = 'Rutas', @Mensaje = 'Registro generado correctamente!', @Posicion = 'toast-top-right';
            GOTO Quit;
        END
        ELSE
        BEGIN
            -- Update existing record
            UPDATE ruta
            SET Ruta = @Ruta,
                Zona = @Zona,
                Kms = @Kms,
                Costo = @Costo,
                SucursalID = @SucursalID,
				DestinoID = @DestinoID,
				OrigenID = @OrigenID,
				 Observaciones = @Observaciones,
                EstatusID = @EstatusID,
                Tiempo = @Tiempo,
                UltimoCambio = GETDATE(),
				Fecha = @Fecha,
				VehiculoID = @VehiculoID,
				CostoInfantil = @CostoInfantil,
				CostoAdulto = @CostoAdulto,
				CostoInapan = @CostoInapan
            WHERE ID = @ID;

            COMMIT TRANSACTION;
            SELECT @Ok = 0, @Tipo = 'success', @Titulo = 'Rutas', @Mensaje = 'Registro actualizado correctamente!', @Posicion = 'toast-top-right';
            GOTO Quit;
        END
    END TRY
    BEGIN CATCH
        ROLLBACK TRANSACTION;
        PRINT ERROR_MESSAGE();
        SELECT @Ok = 1, @Tipo = 'warning', @Titulo = 'Rutas', @Mensaje = 'Error al generar el registro, comuníquese con el administrador!', @Posicion = 'toast-top-right';
        GOTO Quit;
    END CATCH

    Quit:
    SELECT @Ok AS Ok, @Tipo AS Tipo, @Titulo AS Titulo, @Mensaje AS Mensaje, @Posicion AS Posicion;

END
GO
USE [Metodik30]
GO
/****** Object:  StoredProcedure [dbo].[spActHorarioRuta]    Script Date: 20/09/2024 13:56:22 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

ALTER PROCEDURE [dbo].[spActHorarioRuta]
    @ID INT,
    @RutaID INT,
    @HorarioID INT
AS
BEGIN
    DECLARE
        @Ok INT,
        @Tipo VARCHAR(25), -- success, info, warning, error
        @Titulo VARCHAR(250),
        @Mensaje VARCHAR(250),
        @Posicion VARCHAR(25); -- toast + (Top Right, Bottom Right, Bottom Left, Top Left, etc.)

   
    IF @RutaID IS NULL OR @HorarioID IS NULL 
    BEGIN
        SELECT 
            @Ok = 1,
            @Tipo = 'warning',
            @Titulo = 'Horario Ruta',
            @Mensaje = 'Ruta, Horario y Vehículo son obligatorios.',
            @Posicion = 'toast-top-right';
        RETURN;
    END

    BEGIN TRY
        BEGIN TRAN;
            -- Si no existe el registro, inserta uno nuevo
            IF NOT EXISTS (SELECT 1 FROM HorarioRuta WHERE ID = @ID)
            BEGIN
                INSERT INTO HorarioRuta (RutaID, HorarioID)
                VALUES (@RutaID, @HorarioID);

                COMMIT TRAN;
                SELECT 
                    @Ok = 0,
                    @Tipo = 'success',
                    @Titulo = 'Horario Ruta',
                    @Mensaje = 'Registro generado correctamente.',
                    @Posicion = 'toast-top-right';
            END 
            -- Si ya existe, actualiza el registro existente
            ELSE 
            BEGIN
                UPDATE HorarioRuta
                SET 
                    RutaID = @RutaID,
                    HorarioID = @HorarioID
                WHERE ID = @ID;

                COMMIT TRAN;
                SELECT 
                    @Ok = 0,
                    @Tipo = 'success',
                    @Titulo = 'Horario Ruta',
                    @Mensaje = 'Registro actualizado correctamente.',
                    @Posicion = 'toast-top-right';
            END
    END TRY
    BEGIN CATCH
        ROLLBACK TRAN;
        SELECT 
            @Ok = 1,
            @Tipo = 'error',
            @Titulo = 'Horario Ruta',
            @Mensaje = ERROR_MESSAGE(),
            @Posicion = 'toast-top-right';
    END CATCH

    SELECT @Ok AS Ok, @Tipo AS Tipo, @Titulo AS Titulo, @Mensaje AS Mensaje, @Posicion AS Posicion;
END
GO
USE [Metodik30]
GO
/****** Object:  StoredProcedure [dbo].[spVerRutas]    Script Date: 20/09/2024 13:56:48 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
ALTER PROCEDURE [dbo].[spVerRutas]
AS BEGIN 

Select
	ID ,
	ISNULL(Ruta,'') as Ruta,
	ISNULL(Zona,'') as Zona,
	ISNULL(Kms,'') as Kms,
	ISNULL(Costo,0) as Costo,
	ISNULL(SucursalID, 0) as SucursalID,
	ISNULL(DestinoID,0) as DestinoID,
	ISNULL(OrigenID,0) as OrigenID,
	ISNULL(Observaciones,'') as Observaciones,
	ISNULL(EstatusID,0) as EstatusID,
	ISNULL(Tiempo,'') as Tiempo,
	ISNULL(UltimoCambio,'') as UltimoCambio,
	ISNULL(FechaRegistro,'') as FechaRegistro,
	ISNULL(Fecha,'') as Fecha,
	ISNULL(VehiculoID,0) as VehiculoID,
	ISNULL(CostoInfantil,0) as CostoInfantil,
	ISNULL(CostoAdulto,0) as CostoAdulto,
	ISNULL(CostoInapan,0) as CostoInapan
	FROM Ruta 

END
GO
USE [Metodik30]
GO
/****** Object:  StoredProcedure [dbo].[spVerHorarios]    Script Date: 20/09/2024 13:57:21 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

ALTER PROCEDURE [dbo].[spVerHorarios]
AS
BEGIN
    SELECT 
       ID,
       -- Convertir el campo Hora (tipo TIME) a string en formato HH:MM:SS
       CONVERT(VARCHAR(8), Hora, 108) AS HoraString
    FROM Horario
    WHERE EstatusID = 1;
END;
GO
USE [Metodik30]
GO
/****** Object:  StoredProcedure [dbo].[spVerRutasHorarios]    Script Date: 20/09/2024 13:57:41 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
ALTER PROCEDURE [dbo].[spVerRutasHorarios]
    @RutaID int
AS
BEGIN 
    SELECT 
        ID,
        ISNULL(HorarioID, '') AS HorarioID
    FROM 
        HorarioRuta
    WHERE 
        RutaID = @RutaID;
END
GO
USE [Metodik30]
GO
/****** Object:  StoredProcedure [dbo].[spEliminarHorarioRuta]    Script Date: 20/09/2024 13:58:10 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
ALTER PROCEDURE [dbo].[spEliminarHorarioRuta]
    @ID int
AS
BEGIN
    -- Iniciar la transacción
    BEGIN TRY
        BEGIN TRANSACTION;

        -- Eliminar el registro de la tabla HorarioRuta
        DELETE FROM HorarioRuta
        WHERE ID = @ID;

        -- Verificar si algún registro fue afectado
        IF @@ROWCOUNT = 0
        BEGIN
            -- Si no se encontró un registro con ese ID, lanzar un error
            THROW 50000, 'No se encontró un registro con el ID proporcionado.', 1;
        END

        -- Confirmar la transacción
        COMMIT TRANSACTION;

        -- Devolver el mensaje de éxito
        SELECT 'El registro con ID ' + CAST(@ID AS NVARCHAR(10)) + ' ha sido eliminado exitosamente.' AS Mensaje;

    END TRY
    BEGIN CATCH
        -- Si hay un error, deshacer la transacción
        ROLLBACK TRANSACTION;

        -- Manejo de errores
        DECLARE @ErrorMessage NVARCHAR(4000) = ERROR_MESSAGE();
        THROW 50000, @ErrorMessage, 1;
    END CATCH
END
GO